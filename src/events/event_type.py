import pygame

from enum import Enum


class EventType(Enum):
    ACTIVE_EVENT = pygame.ACTIVEEVENT  # gain, state (DEPRECATED)
    AUDIO_DEVICE_ADDED = pygame.AUDIODEVICEADDED  # which, iscapture (SDL backend >= 2.0.4)  
    AUDIO_DEVICE_REMOVED = pygame.AUDIODEVICEREMOVED  # which, iscapture (SDL backend >= 2.0.4)  
    CLIPBOARD_UPDATE = pygame.CLIPBOARDUPDATE  #
    CONTROLLER_DEVICE_ADDED = pygame.CONTROLLERDEVICEADDED  # device_index
    CONTROLLER_DEVICE_REMAPPED = pygame.CONTROLLERDEVICEREMAPPED  # instance_id
    CONTROLLER_DEVICE_REMOVED = pygame.CONTROLLERDEVICEREMOVED  # instance_id
    DROP_BEGIN = pygame.DROPBEGIN  # (SDL backend >= 2.0.5)
    DROP_COMPLETE = pygame.DROPCOMPLETE  # (SDL backend >= 2.0.5)
    DROP_FILE = pygame.DROPFILE  # file
    DROP_TEXT = pygame.DROPTEXT  # text (SDL backend >= 2.0.5) (X11)
    FINGER_DOWN = pygame.FINGERDOWN  # touch_id, finger_id, x, y, dx, dy  
    FINGER_MOTION = pygame.FINGERMOTION  # touch_id, finger_id, x, y, dx, dy  
    FINGER_UP = pygame.FINGERUP  # touch_id, finger_id, x, y, dx, dy  
    JOY_AXIS_MOTION = pygame.JOYAXISMOTION  # instance_id, axis, value
    JOY_BALL_MOTION = pygame.JOYBALLMOTION  # instance_id, ball, rel
    JOY_BUTTON_UP = pygame.JOYBUTTONUP  # instance_id, button
    JOY_BUTTON_DOWN = pygame.JOYBUTTONDOWN  # instance_id, button
    JOY_DEVICE_ADDED = pygame.JOYDEVICEADDED  # device_index
    JOY_DEVICE_REMOVED = pygame.JOYDEVICEREMOVED  # instance_id
    JOY_HAT_MOTION = pygame.JOYHATMOTION  # instance_id, hat, value
    KEYMAP_CHANGED = pygame.KEYMAPCHANGED  # (SDL backend >= 2.0.4)
    KEY_DOWN = pygame.KEYDOWN  # key, mod, unicode, scancode
    KEY_UP = pygame.KEYUP  # key, mod, unicode, scancode
    LOCALE_CHANGED = pygame.LOCALECHANGED  # (SDL backend >= 2.0.14)
    MIDI_IN = pygame.MIDIIN  # pygame.midi
    MIDI_OUT = pygame.MIDIOUT  # pygame.midi
    MOUSE_BUTTON_DOWN = pygame.MOUSEBUTTONDOWN  # pos, button, touch
    MOUSE_BUTTON_UP = pygame.MOUSEBUTTONUP  # pos, button, touch
    MOUSE_MOTION = pygame.MOUSEMOTION  # pos, rel, buttons, touch
    MOUSE_WHEEL = pygame.MOUSEWHEEL  # which, flipped, x, y, touch, precise_x, precise_y  
    MULTI_GESTURE = pygame.MULTIGESTURE  # touch_id, x, y, pinched, rotated, num_fingers  
    QUIT = pygame.QUIT  # none
    RENDER_DEVICE_RESET = pygame.RENDER_DEVICE_RESET  # (SDL backend >= 2.0.4)
    RENDER_TARGETS_RESET = pygame.RENDER_TARGETS_RESET  # (SDL backend >= 2.0.2)
    TEXT_EDITING = pygame.TEXTEDITING  # text, start, length  
    TEXT_INPUT = pygame.TEXTINPUT  # text  
    USER_EVENT = pygame.USEREVENT  # code
    VIDEO_EXPOSE = pygame.VIDEOEXPOSE  # none (DEPRECATED)
    VIDEO_RESIZE = pygame.VIDEORESIZE  # size, w, h (DEPRECATED)
    WINDOW_CLOSE = pygame.WINDOWCLOSE  # Window was closed
    WINDOW_DISPLAY_CHANGED = pygame.WINDOWDISPLAYCHANGED  # Window moved on a new display (SDL backend >= 2.0.18)
    WINDOW_ENTER = pygame.WINDOWENTER  # Mouse entered the window
    WINDOW_EXPOSED = pygame.WINDOWEXPOSED  # Window got updated by some external event
    WINDOW_FOCUS_GAINED = pygame.WINDOWFOCUSGAINED  # Window gained focus
    WINDOW_FOCUS_LOST = pygame.WINDOWFOCUSLOST  # Window lost focus
    WINDOW_HIDDEN = pygame.WINDOWHIDDEN  # Window became hidden
    WINDOW_HIT_TEST = pygame.WINDOWHITTEST  # Window has a special hit test (SDL backend >= 2.0.5)
    WINDOW_ICC_PROFILE_CHANGED = pygame.WINDOWICCPROFCHANGED  # Window ICC profile changed (SDL backend >= 2.0.18)
    WINDOW_LEAVE = pygame.WINDOWLEAVE  # Mouse left the window
    WINDOW_MAXIMIZED = pygame.WINDOWMAXIMIZED  # Window was maximized
    WINDOW_MINIMIZED = pygame.WINDOWMINIMIZED  # Window was minimized
    WINDOW_MOVED = pygame.WINDOWMOVED  # Window got moved
    WINDOW_RESIZED = pygame.WINDOWRESIZED  # Window got resized
    WINDOW_RESTORED = pygame.WINDOWRESTORED  # Window was restored
    WINDOW_SHOWN = pygame.WINDOWSHOWN  # Window became shown
    WINDOW_SIZE_CHANGED = pygame.WINDOWSIZECHANGED  # Window changed its size
    WINDOW_TAKE_FOCUS = pygame.WINDOWTAKEFOCUS  # Window was offered focus (SDL backend >= 2.0.5)
