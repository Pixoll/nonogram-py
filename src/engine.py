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
                event = Engine._parse_event(raw_event)
                print(event)

                self.screen.on_event(event)

                if event.type == events.EventType.QUIT:
                    running = False

            window.fill("white")
            self.screen.render()
            pygame.display.flip()

            clock.tick(60)

    @staticmethod
    def _parse_event(event: pygame.event.Event) -> events.Event:
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
            case pygame.JOYBUTTONDOWN:
                return events.JoyButtonDownEvent(event)
            case pygame.JOYBUTTONUP:
                return events.JoyButtonUpEvent(event)
            case pygame.JOYDEVICEADDED:
                return events.JoyDeviceAddedEvent(event)
            case pygame.JOYDEVICEREMOVED:
                return events.JoyDeviceRemovedEvent(event)
            case pygame.JOYHATMOTION:
                return events.JoyHatMotionEvent(event)
            case pygame.KEYMAPCHANGED:
                return events.KeymapChangedEvent(event)
            case pygame.KEYDOWN:
                return events.KeyDownEvent(event)
            case pygame.KEYUP:
                return events.KeyUpEvent(event)
            case pygame.LOCALECHANGED:
                return events.LocaleChangedEvent(event)
            case pygame.MIDIIN:
                return events.MidiInEvent(event)
            case pygame.MIDIOUT:
                return events.MidiOutEvent(event)
            case pygame.MOUSEBUTTONDOWN:
                return events.MouseButtonDownEvent(event)
            case pygame.MOUSEBUTTONUP:
                return events.MouseButtonUpEvent(event)
            case pygame.MOUSEMOTION:
                return events.MouseMotionEvent(event)
            case pygame.MOUSEWHEEL:
                return events.MouseWheelEvent(event)
            case pygame.MULTIGESTURE:
                return events.MultiGestureEvent(event)
            case pygame.QUIT:
                return events.QuitEvent(event)
            case pygame.RENDER_DEVICE_RESET:
                return events.RenderDeviceResetEvent(event)
            case pygame.RENDER_TARGETS_RESET:
                return events.RenderTargetsResetEvent(event)
            case pygame.TEXTEDITING:
                return events.TextEditingEvent(event)
            case pygame.TEXTINPUT:
                return events.TextInputEvent(event)
            case pygame.USEREVENT:
                return events.UserEvent(event)
            case pygame.VIDEOEXPOSE:
                return events.VideoExposeEvent(event)
            case pygame.VIDEORESIZE:
                return events.VideoResizeEvent(event)
            case pygame.WINDOWCLOSE:
                return events.WindowCloseEvent(event)
            case pygame.WINDOWDISPLAYCHANGED:
                return events.WindowDisplayChangedEvent(event)
            case pygame.WINDOWENTER:
                return events.WindowEnterEvent(event)
            case pygame.WINDOWEXPOSED:
                return events.WindowExposedEvent(event)
            case pygame.WINDOWFOCUSGAINED:
                return events.WindowFocusGainedEvent(event)
            case pygame.WINDOWFOCUSLOST:
                return events.WindowFocusLostEvent(event)
            case pygame.WINDOWHIDDEN:
                return events.WindowHiddenEvent(event)
            case pygame.WINDOWHITTEST:
                return events.WindowHitTestEvent(event)
            case pygame.WINDOWICCPROFCHANGED:
                return events.WindowIccProfileChangedEvent(event)
            case pygame.WINDOWLEAVE:
                return events.WindowLeaveEvent(event)
            case pygame.WINDOWMAXIMIZED:
                return events.WindowMaximizedEvent(event)
            case pygame.WINDOWMINIMIZED:
                return events.WindowMinimizedEvent(event)
            case pygame.WINDOWMOVED:
                return events.WindowMovedEvent(event)
            case pygame.WINDOWRESIZED:
                return events.WindowResizedEvent(event)
            case pygame.WINDOWRESTORED:
                return events.WindowRestoredEvent(event)
            case pygame.WINDOWSHOWN:
                return events.WindowShownEvent(event)
            case pygame.WINDOWSIZECHANGED:
                return events.WindowSizeChangedEvent(event)
            case pygame.WINDOWTAKEFOCUS:
                return events.WindowTakeFocusEvent(event)
