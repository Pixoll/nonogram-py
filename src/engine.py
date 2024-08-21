import pygame

import events
from screens.screen import Screen


class Engine:
    screen: Screen

    def __init__(self):
        pass

    def set_screen(self, screen: Screen) -> None:
        self.screen = screen

    def run(self, window: pygame.Surface, clock: pygame.time.Clock) -> None:
        if not hasattr(self, "screen"):
            raise Exception("No screen")

        running = True

        while running:
            for raw_event in pygame.event.get():
                print(raw_event)
                event = Engine._parse_event(raw_event)
                print(event)
                print()

                if event is None:
                    continue

                self.screen.on_event(event)

                if event.type == events.EventType.QUIT:
                    running = False

            window.fill("white")
            self.screen.render()
            pygame.display.flip()

            clock.tick(60)

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
