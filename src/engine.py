import pygame
from pygame.font import Font

import events
from assets import FontManager
from screens.screen import Screen


class Engine:
    _screen: Screen | None
    _window: pygame.Surface
    _big_font: Font
    _regular_font: Font
    _small_font: Font

    def __init__(self, window: pygame.Surface):
        self._screen = None
        self._window = window
        width = self._window.get_width()
        self._big_font = FontManager.get_default(int(width * 0.0225))
        self._regular_font = FontManager.get_default(int(width * 0.015))
        self._small_font = FontManager.get_default(int(width * 0.0075))

    def set_screen(self, screen: Screen) -> None:
        self._screen = screen

    @property
    def window_size(self) -> tuple[int, int]:
        return self._window.get_size()

    @property
    def big_font(self) -> Font:
        return self._big_font

    @property
    def regular_font(self) -> Font:
        return self._regular_font

    @property
    def small_font(self) -> Font:
        return self._small_font

    def run(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        if self._screen is None:
            raise ValueError("No screen - use set_screen() before run()")

        running = True

        while running:
            for raw_event in pygame.event.get():
                event = Engine._parse_event(raw_event)
                if event is None:
                    continue

                self._screen.on_any_event(event)
                self._delegate_event(event)

                if event.type == events.EventType.QUIT:
                    running = False

            window.fill("white")
            self._screen.render()
            pygame.display.flip()

            clock.tick(60)

    def _delegate_event(self, event: events.Event) -> None:
        match event.type:
            case events.EventType.KEY_UP | events.EventType.KEY_DOWN:
                self._screen.on_key_event(event)
            case events.EventType.MOUSE_BUTTON_UP | events.EventType.MOUSE_BUTTON_DOWN:
                self._screen.on_mouse_button_event(event)
            case events.EventType.MOUSE_MOTION:
                self._screen.on_mouse_motion_event(event)
            case events.EventType.QUIT:
                self._screen.on_quit_event(event)

    @staticmethod
    def _parse_event(event: pygame.event.Event) -> events.Event | None:
        match event.type:
            case pygame.ACTIVEEVENT:
                return events.ActiveEvent(event)
            case pygame.AUDIODEVICEADDED | pygame.AUDIODEVICEREMOVED:
                return events.AudioDeviceEvent(event)
            case pygame.CLIPBOARDUPDATE:
                return events.ClipboardUpdateEvent()
            case pygame.CONTROLLERDEVICEADDED | pygame.CONTROLLERDEVICEREMAPPED | pygame.CONTROLLERDEVICEREMOVED:
                return events.ControllerDeviceEvent(event)
            case pygame.DROPBEGIN | pygame.DROPCOMPLETE:
                return events.DropStatusEvent(event)
            case pygame.DROPFILE:
                return events.DropFileEvent(event)
            case pygame.DROPTEXT:
                return events.DropTextEvent(event)
            case pygame.FINGERDOWN | pygame.FINGERMOTION | pygame.FINGERUP:
                return events.FingerEvent(event)
            case pygame.JOYAXISMOTION:
                return events.JoyAxisMotionEvent(event)
            case pygame.JOYBALLMOTION:
                return events.JoyBallMotionEvent(event)
            case pygame.JOYBUTTONDOWN | pygame.JOYBUTTONUP:
                return events.JoyButtonEvent(event)
            case pygame.JOYDEVICEADDED | pygame.JOYDEVICEREMOVED:
                return events.JoyDeviceEvent(event)
            case pygame.JOYHATMOTION:
                return events.JoyHatMotionEvent(event)
            case pygame.KEYMAPCHANGED:
                return events.KeymapChangedEvent()
            case pygame.KEYDOWN | pygame.KEYUP:
                return events.KeyEvent(event)
            case pygame.LOCALECHANGED:
                return events.LocaleChangedEvent()
            case pygame.MIDIIN | pygame.MIDIOUT:
                return events.MidiEvent(event)
            case pygame.MOUSEBUTTONDOWN | pygame.MOUSEBUTTONUP:
                return events.MouseButtonEvent(event)
            case pygame.MOUSEMOTION:
                return events.MouseMotionEvent(event)
            case pygame.MOUSEWHEEL:
                return events.MouseWheelEvent(event)
            case pygame.MULTIGESTURE:
                return events.MultiGestureEvent(event)
            case pygame.QUIT:
                return events.QuitEvent()
            case pygame.RENDER_DEVICE_RESET:
                return events.RenderDeviceResetEvent()
            case pygame.RENDER_TARGETS_RESET:
                return events.RenderTargetsResetEvent()
            case pygame.TEXTEDITING:
                return events.TextEditingEvent(event)
            case pygame.TEXTINPUT:
                return events.TextInputEvent(event)
            case pygame.USEREVENT:
                return events.UserEvent(event)
            case pygame.VIDEOEXPOSE:
                return events.VideoExposeEvent()
            case pygame.VIDEORESIZE:
                return events.VideoResizeEvent(event)
            case (pygame.WINDOWCLOSE
                  | pygame.WINDOWDISPLAYCHANGED
                  | pygame.WINDOWENTER
                  | pygame.WINDOWEXPOSED
                  | pygame.WINDOWFOCUSGAINED
                  | pygame.WINDOWFOCUSLOST
                  | pygame.WINDOWHIDDEN
                  | pygame.WINDOWHITTEST
                  | pygame.WINDOWICCPROFCHANGED
                  | pygame.WINDOWLEAVE
                  | pygame.WINDOWMAXIMIZED
                  | pygame.WINDOWMINIMIZED
                  | pygame.WINDOWMOVED
                  | pygame.WINDOWRESIZED
                  | pygame.WINDOWRESTORED
                  | pygame.WINDOWSHOWN
                  | pygame.WINDOWSIZECHANGED
                  | pygame.WINDOWTAKEFOCUS):
                return events.WindowEvent(event)
            case _:
                print(f"Unknown event: {event}")
                return None
