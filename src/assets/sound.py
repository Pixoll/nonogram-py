from pygame import mixer
from pygame.mixer import SoundType

mixer.init()


class SoundManager:
    _BASE_DIR = "assets/sounds/"

    _SOUNDS: dict[str, SoundType] = {}

    @staticmethod
    def play_music(file_name: str, volume: float = 0.3):
        mixer.music.unload()
        mixer.music.load(SoundManager._BASE_DIR + file_name)
        mixer.music.set_volume(volume)
        mixer.music.play(-1, fade_ms=2000)

    @staticmethod
    def play_sound(file_name: str, volume: float = 0.3):
        if file_name not in SoundManager._SOUNDS:
            SoundManager._SOUNDS[file_name] = mixer.Sound(SoundManager._BASE_DIR + "menu_click.mp3")

        sound = SoundManager._SOUNDS[file_name]
        sound.set_volume(volume)
        sound.play()

    @staticmethod
    def stop_music():
        mixer.music.fadeout(2000)

    @staticmethod
    def stop_sounds():
        mixer.fadeout(1000)

    @staticmethod
    def stop_all():
        SoundManager.stop_music()
        SoundManager.stop_sounds()
