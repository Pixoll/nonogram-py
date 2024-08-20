from enum import Enum

import pygame


class EventType(Enum):
    ACTIVE_EVENT = pygame.ACTIVEEVENT
    """
    **DEPRECATED**
    
    Attributes: gain, state
    """

    AUDIO_DEVICE_ADDED = pygame.AUDIODEVICEADDED
    """
    **SDL backend >= 2.0.4**
    
    Attributes: which, is_capture
    """

    AUDIO_DEVICE_REMOVED = pygame.AUDIODEVICEREMOVED
    """
    **SDL backend >= 2.0.4**
    
    Attributes: which, is_capture
    """

    CLIPBOARD_UPDATE = pygame.CLIPBOARDUPDATE
    """
    Attributes: none
    """

    CONTROLLER_DEVICE_ADDED = pygame.CONTROLLERDEVICEADDED
    """
    Attributes: device_index
    """

    CONTROLLER_DEVICE_REMAPPED = pygame.CONTROLLERDEVICEREMAPPED
    """
    Attributes: instance_id
    """

    CONTROLLER_DEVICE_REMOVED = pygame.CONTROLLERDEVICEREMOVED
    """
    Attributes: instance_id
    """

    DROP_BEGIN = pygame.DROPBEGIN
    """
    **SDL backend >= 2.0.5**
    """

    DROP_COMPLETE = pygame.DROPCOMPLETE
    """
    **SDL backend >= 2.0.5**
    """

    DROP_FILE = pygame.DROPFILE
    """
    Attributes: file
    """

    DROP_TEXT = pygame.DROPTEXT
    """
    **SDL backend >= 2.0.5 | X11 | Linux**
    
    Attributes: text
    """

    FINGER_DOWN = pygame.FINGERDOWN
    """
    Attributes: touch_id, finger_id, x, y, dx, dy  
    """

    FINGER_MOTION = pygame.FINGERMOTION
    """
    Attributes: touch_id, finger_id, x, y, dx, dy  
    """

    FINGER_UP = pygame.FINGERUP
    """
    Attributes: touch_id, finger_id, x, y, dx, dy  
    """

    JOY_AXIS_MOTION = pygame.JOYAXISMOTION
    """
    Attributes: instance_id, axis, value
    """

    JOY_BALL_MOTION = pygame.JOYBALLMOTION
    """
    Attributes: instance_id, ball, rel
    """

    JOY_BUTTON_DOWN = pygame.JOYBUTTONDOWN
    """
    Attributes: instance_id, button
    """

    JOY_BUTTON_UP = pygame.JOYBUTTONUP
    """
    Attributes: instance_id, button
    """

    JOY_DEVICE_ADDED = pygame.JOYDEVICEADDED
    """
    Attributes: device_index
    """

    JOY_DEVICE_REMOVED = pygame.JOYDEVICEREMOVED
    """
    Attributes: instance_id
    """

    JOY_HAT_MOTION = pygame.JOYHATMOTION
    """
    Attributes: instance_id, hat, value
    """

    KEYMAP_CHANGED = pygame.KEYMAPCHANGED
    """
    **SDL backend >= 2.0.4**
    """

    KEY_DOWN = pygame.KEYDOWN
    """
    Attributes: key, mod, unicode, scancode
    """

    KEY_UP = pygame.KEYUP
    """
    Attributes: key, mod, unicode, scancode
    """

    LOCALE_CHANGED = pygame.LOCALECHANGED
    """
    **SDL backend >= 2.0.14**
    """

    MIDI_IN = pygame.MIDIIN
    """
    Exclusively for pygame.midi
    """

    MIDI_OUT = pygame.MIDIOUT
    """
    Exclusively for pygame.midi
    """

    MOUSE_BUTTON_DOWN = pygame.MOUSEBUTTONDOWN
    """
    Attributes: pos, button, touch
    """

    MOUSE_BUTTON_UP = pygame.MOUSEBUTTONUP
    """
    Attributes: pos, button, touch
    """

    MOUSE_MOTION = pygame.MOUSEMOTION
    """
    Attributes: pos, rel, buttons, touch
    """

    MOUSE_WHEEL = pygame.MOUSEWHEEL
    """
    Attributes: which, flipped, x, y, touch, precise_x, precise_y
    """

    MULTI_GESTURE = pygame.MULTIGESTURE
    """
    Attributes: touch_id, x, y, pinched, rotated, num_fingers  
    """

    QUIT = pygame.QUIT
    """
    Attributes: none
    """

    RENDER_DEVICE_RESET = pygame.RENDER_DEVICE_RESET
    """
    **SDL backend >= 2.0.4**
    """

    RENDER_TARGETS_RESET = pygame.RENDER_TARGETS_RESET
    """
    **SDL backend >= 2.0.2**
    """

    TEXT_EDITING = pygame.TEXTEDITING
    """
    Attributes: text, start, length  
    """

    TEXT_INPUT = pygame.TEXTINPUT
    """
    Attributes: text  
    """

    USER_EVENT = pygame.USEREVENT
    """
    Attributes: code
    """

    VIDEO_EXPOSE = pygame.VIDEOEXPOSE
    """
    **DEPRECATED**
    
    Attributes: none
    """

    VIDEO_RESIZE = pygame.VIDEORESIZE
    """
    **DEPRECATED**
    
    Attributes: size, w, h
    """

    WINDOW_CLOSE = pygame.WINDOWCLOSE
    """
    Window was closed
    """

    WINDOW_DISPLAY_CHANGED = pygame.WINDOWDISPLAYCHANGED
    """
    **SDL backend >= 2.0.18**
    
    Window moved on a new display
    """

    WINDOW_ENTER = pygame.WINDOWENTER
    """
    Mouse entered the window
    """

    WINDOW_EXPOSED = pygame.WINDOWEXPOSED
    """
    Window got updated by some external event
    """

    WINDOW_FOCUS_GAINED = pygame.WINDOWFOCUSGAINED
    """
    Window gained focus
    """

    WINDOW_FOCUS_LOST = pygame.WINDOWFOCUSLOST
    """
    Window lost focus
    """

    WINDOW_HIDDEN = pygame.WINDOWHIDDEN
    """
    Window became hidden
    """

    WINDOW_HIT_TEST = pygame.WINDOWHITTEST
    """
    **SDL backend >= 2.0.5**
    
    Window has a special hit test
    """

    WINDOW_ICC_PROFILE_CHANGED = pygame.WINDOWICCPROFCHANGED
    """
    **SDL backend >= 2.0.18**
    
    Window ICC profile changed
    """

    WINDOW_LEAVE = pygame.WINDOWLEAVE
    """
    Mouse left the window
    """

    WINDOW_MAXIMIZED = pygame.WINDOWMAXIMIZED
    """
    Window was maximized
    """

    WINDOW_MINIMIZED = pygame.WINDOWMINIMIZED
    """
    Window was minimized
    """

    WINDOW_MOVED = pygame.WINDOWMOVED
    """
    Window got moved
    """

    WINDOW_RESIZED = pygame.WINDOWRESIZED
    """
    Window got resized
    """

    WINDOW_RESTORED = pygame.WINDOWRESTORED
    """
    Window was restored
    """

    WINDOW_SHOWN = pygame.WINDOWSHOWN
    """
    Window became shown
    """

    WINDOW_SIZE_CHANGED = pygame.WINDOWSIZECHANGED
    """
    Window changed its size
    """

    WINDOW_TAKE_FOCUS = pygame.WINDOWTAKEFOCUS
    """
    **SDL backend >= 2.0.5**
    
    Window was offered focus
    """
