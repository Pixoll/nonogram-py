from pygame import mixer

mixer.init()


class Sound:
    _MENU_CLICK = mixer.Sound("assets/sounds/menu_click.mp3")
    _GAME_CLICK = mixer.Sound("assets/sounds/click.mp3")

    @staticmethod
    def play_background_music(volume: float = 0.3):
        mixer.music.load("assets/sounds/music.mp3")
        mixer.music.set_volume(volume)
        mixer.music.play(-1, fade_ms=2000)

    @staticmethod
    def play_menu_click(volume: float = 0.3):
        Sound._MENU_CLICK.set_volume(volume)
        Sound._MENU_CLICK.play()

    @staticmethod
    def play_game_click(volume: float = 0.3):
        Sound._GAME_CLICK.set_volume(volume)
        Sound._GAME_CLICK.play()

    @staticmethod
    def stop_music():
        mixer.music.fadeout(2000)

    @staticmethod
    def stop_sounds():
        mixer.fadeout(1000)

    @staticmethod
    def stop_all():
        Sound.stop_music()
        Sound.stop_sounds()
