from typing import Literal, TypeAlias

rgb_t: TypeAlias = tuple[int, int, int]
nonogram_type_t: TypeAlias = Literal["pre_made", "user_made"]
nonogram_matrix_t: TypeAlias = list[list[rgb_t | None]]
