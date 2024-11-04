from collections import OrderedDict
from os.path import exists

from core.nonogram import Nonogram
from core.types import nonogram_matrix_t, nonogram_type_t, rgb_t


# noinspection PyProtectedMember
class NonogramLoader:
    _PRE_MADE: OrderedDict[int, Nonogram | None] = OrderedDict()
    _PRE_MADE_BIN = bytearray()
    _PRE_MADE_BIN_INDEX: OrderedDict[int, tuple[int, int]] = OrderedDict()

    _USER_MADE: OrderedDict[int, Nonogram | None] = OrderedDict()
    _USER_MADE_BIN = bytearray()
    _USER_MADE_BIN_INDEX: OrderedDict[int, tuple[int, int]] = OrderedDict()

    @staticmethod
    def preload_nonograms() -> None:
        NonogramLoader._preload_nonograms_of_type("pre_made")
        NonogramLoader._preload_nonograms_of_type("user_made")

    @staticmethod
    def load(nonogram_type: nonogram_type_t, nonogram_id: int) -> Nonogram:
        nonograms_dict = NonogramLoader._PRE_MADE if nonogram_type == "pre_made" else NonogramLoader._USER_MADE

        if nonogram_id not in nonograms_dict:
            raise ValueError(f"Nonogram of type {nonogram_type} with id {nonogram_id} does not exist.")

        if nonograms_dict[nonogram_id] is not None:
            return nonograms_dict[nonogram_id]

        nonograms_bin = NonogramLoader._PRE_MADE_BIN if nonogram_type == "pre_made" else NonogramLoader._USER_MADE_BIN
        nonograms_bin_index = (NonogramLoader._PRE_MADE_BIN_INDEX if nonogram_type == "pre_made"
                               else NonogramLoader._USER_MADE_BIN_INDEX)

        index, size = nonograms_bin_index[nonogram_id]
        nonogram = NonogramLoader._deserialize(nonogram_type, nonograms_bin[index + 2: index + size + 2])
        nonograms_dict[nonogram_id] = nonogram

        return nonogram

    @staticmethod
    def save(nonogram_type: nonogram_type_t, nonogram_id: int) -> None:
        nonograms_dict = NonogramLoader._PRE_MADE if nonogram_type == "pre_made" else NonogramLoader._USER_MADE
        nonograms_bin = NonogramLoader._PRE_MADE_BIN if nonogram_type == "pre_made" else NonogramLoader._USER_MADE_BIN
        nonograms_bin_index = (NonogramLoader._PRE_MADE_BIN_INDEX if nonogram_type == "pre_made"
                               else NonogramLoader._USER_MADE_BIN_INDEX)

        if nonogram_id not in nonograms_dict:
            raise ValueError(f"Nonogram of type {nonogram_type} with id {nonogram_id} does not exist.")

        nonogram = nonograms_dict[nonogram_id]

        if nonogram is None:
            raise ValueError(f"Nonogram of type {nonogram_type} with id {nonogram_id} has not been loaded yet.")

        file_path = f"nonograms/{nonogram_type}.bin"

        index, size = nonograms_bin_index[nonogram_id]
        serialized, new_size = NonogramLoader._serialize(nonogram)

        nonograms_bin[index:index + size + 2] = serialized
        nonograms_bin_index[nonogram_id] = (index, new_size)

        with open(file_path, mode="rb") as file:
            file.write(nonograms_bin)

    @staticmethod
    def store_and_save(nonogram: Nonogram) -> int:
        new_id = next(reversed(NonogramLoader._USER_MADE)) if len(NonogramLoader._USER_MADE) > 0 else 1
        nonogram._id = new_id

        serialized, size = NonogramLoader._serialize(nonogram)

        NonogramLoader._USER_MADE[new_id] = nonogram
        NonogramLoader._USER_MADE_BIN.extend(serialized)
        NonogramLoader._USER_MADE_BIN_INDEX[new_id] = (len(NonogramLoader._USER_MADE_BIN), size)

        return new_id

    @staticmethod
    def _preload_nonograms_of_type(nonogram_type: nonogram_type_t) -> None:
        nonograms_dict = NonogramLoader._PRE_MADE if nonogram_type == "pre_made" else NonogramLoader._USER_MADE
        nonograms_bin = NonogramLoader._PRE_MADE_BIN if nonogram_type == "pre_made" else NonogramLoader._USER_MADE_BIN
        nonograms_bin_index = (NonogramLoader._PRE_MADE_BIN_INDEX if nonogram_type == "pre_made"
                               else NonogramLoader._USER_MADE_BIN_INDEX)

        file_path = f"nonograms/{nonogram_type}.bin"

        nonograms_dict.clear()
        nonograms_bin.clear()
        nonograms_bin_index.clear()

        if not exists(file_path):
            return

        with open(file_path, mode="rb") as file:
            nonograms_bin.extend(bytearray(file.read()))

        i = 0

        while i < len(nonograms_bin):
            size = int.from_bytes(nonograms_bin[i:i + 2], byteorder="big", signed=False)
            nonogram_id = int.from_bytes(nonograms_bin[i + 2:i + 5], byteorder="big", signed=False)

            nonograms_dict[nonogram_id] = None
            nonograms_bin_index[nonogram_id] = (i, size)

            i += size + 2

    @staticmethod
    def _serialize(nonogram: Nonogram) -> tuple[bytearray, int]:
        if nonogram._id is None or nonogram._name is None:
            raise ValueError("Nonogram id and name must be present when serializing.")

        for y in range(nonogram._size[1]):
            for x in range(nonogram._size[0]):
                nonogram[x, y] = nonogram._original[y][x]

        inverse_palette: dict[rgb_t, int] = {v: int(k) + 1 for k, v in nonogram._palette.items()}
        binary = len(inverse_palette) == 1

        original_mask: list[int] = []
        player_mask: list[int] = []
        empty = True
        completed = nonogram.is_completed

        bit = 7
        byte = 0

        for y in range(nonogram._size[1]):
            for x in range(nonogram._size[0]):
                original_cell = nonogram._original[y][x]
                if binary:
                    byte |= (original_cell is not None) << bit
                    bit -= 1

                    if bit < 0:
                        original_mask.append(byte)
                        bit = 7
                        byte = 0
                else:
                    original_mask.append(
                        0 if original_cell is None
                        else inverse_palette[original_cell]
                    )

                player_cell = nonogram._player_grid[y][x]
                if player_cell is not None:
                    empty = False

                # noinspection PyTypeChecker
                player_mask.append(
                    0 if player_cell is None
                    else 1 if player_cell == "x"
                    else inverse_palette[player_cell]
                )

        if bit != 7:
            original_mask.append(byte)

        result = bytearray()

        # distribute id on 3 bytes, max of 16 777 215 ids
        result.extend(nonogram._id.to_bytes(3, byteorder="big", signed=False))
        result.extend(nonogram._size)
        result.append(len(inverse_palette))
        result.append(empty)
        result.append(nonogram.is_completed)

        result.extend(nonogram._name.encode())
        result.append(0)

        for color in inverse_palette.keys():
            result.extend(color)

        result.extend(original_mask)

        if not empty and not completed:
            result.extend(player_mask)

        result_size = len(result)
        result_size_bytes = len(result).to_bytes(2, byteorder="big", signed=False)
        result.insert(0, result_size_bytes[1])
        result.insert(0, result_size_bytes[0])

        return result, result_size

    @staticmethod
    def _deserialize(nonogram_type: nonogram_type_t, data: bytearray) -> Nonogram:
        nonogram_id = int.from_bytes(data[:3], byteorder="big", signed=False)
        width = data[3]
        height = data[4]
        colors_len = data[5]
        empty = bool(data[6])
        completed = bool(data[7])

        binary = colors_len == 1

        i = 8
        while data[i] != 0:
            i += 1

        name = data[8:i].decode()

        i += 1
        palette: dict[int, rgb_t] = {}

        for j in range(colors_len):
            palette[j + 2] = (data[i], data[i + 1], data[i + 2])
            i += 3

        nonogram_data: nonogram_matrix_t = []
        bit = 7

        for y in range(height):
            nonogram_data.append([])
            for x in range(width):
                cell = data[i]
                if binary:
                    colored = bool((cell >> bit) & 1)
                    nonogram_data[y].append(palette[2] if colored else None)
                    bit -= 1

                    if bit < 0:
                        bit = 7
                        i += 1
                else:
                    nonogram_data[y].append(palette[cell] if cell > 0 else None)
                    i += 1

        nonogram = Nonogram(nonogram_data, nonogram_type, nonogram_id, name, {
            str(k): v for k, v in palette.items()
        })

        if empty:
            return nonogram

        if completed:
            for y in range(height):
                for x in range(width):
                    nonogram[x, y] = nonogram_data[y][x]

            return nonogram

        for y in range(height):
            for x in range(width):
                cell = data[i]
                nonogram[x, y] = None if cell == 0 else "x" if cell == 1 else palette[cell]

        return nonogram


NonogramLoader.preload_nonograms()
