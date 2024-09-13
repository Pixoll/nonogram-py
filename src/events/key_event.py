from enum import Enum
from typing import Literal, Self

import pygame

from events.event_type import EventType


class Key(Enum):
    INVALID = -1
    N0 = pygame.K_0
    N1 = pygame.K_1
    N2 = pygame.K_2
    N3 = pygame.K_3
    N4 = pygame.K_4
    N5 = pygame.K_5
    N6 = pygame.K_6
    N7 = pygame.K_7
    N8 = pygame.K_8
    N9 = pygame.K_9
    A = pygame.K_a
    AC_BACK = pygame.K_AC_BACK
    AMPERSAND = pygame.K_AMPERSAND
    ASTERISK = pygame.K_ASTERISK
    AT = pygame.K_AT
    B = pygame.K_b
    BACKQUOTE = pygame.K_BACKQUOTE
    BACKSLASH = pygame.K_BACKSLASH
    BACKSPACE = pygame.K_BACKSPACE
    BREAK = pygame.K_BREAK
    C = pygame.K_c
    CAPSLOCK = pygame.K_CAPSLOCK
    CARET = pygame.K_CARET
    CLEAR = pygame.K_CLEAR
    COLON = pygame.K_COLON
    COMMA = pygame.K_COMMA
    CURRENCY_SUBUNIT = pygame.K_CURRENCYSUBUNIT
    CURRENCY_UNIT = pygame.K_CURRENCYUNIT
    D = pygame.K_d
    DELETE = pygame.K_DELETE
    DOLLAR = pygame.K_DOLLAR
    DOWN = pygame.K_DOWN
    E = pygame.K_e
    END = pygame.K_END
    EQUALS = pygame.K_EQUALS
    ESCAPE = pygame.K_ESCAPE
    EURO = pygame.K_EURO
    EXCLAIM = pygame.K_EXCLAIM
    F = pygame.K_f
    F1 = pygame.K_F1
    F10 = pygame.K_F10
    F11 = pygame.K_F11
    F12 = pygame.K_F12
    F13 = pygame.K_F13
    F14 = pygame.K_F14
    F15 = pygame.K_F15
    F2 = pygame.K_F2
    F3 = pygame.K_F3
    F4 = pygame.K_F4
    F5 = pygame.K_F5
    F6 = pygame.K_F6
    F7 = pygame.K_F7
    F8 = pygame.K_F8
    F9 = pygame.K_F9
    G = pygame.K_g
    GREATER = pygame.K_GREATER
    H = pygame.K_h
    HASH = pygame.K_HASH
    HELP = pygame.K_HELP
    HOME = pygame.K_HOME
    I = pygame.K_i
    INSERT = pygame.K_INSERT
    J = pygame.K_j
    K = pygame.K_k
    KP0 = pygame.K_KP0
    KP1 = pygame.K_KP1
    KP2 = pygame.K_KP2
    KP3 = pygame.K_KP3
    KP4 = pygame.K_KP4
    KP5 = pygame.K_KP5
    KP6 = pygame.K_KP6
    KP7 = pygame.K_KP7
    KP8 = pygame.K_KP8
    KP9 = pygame.K_KP9
    KP_0 = pygame.K_KP_0
    KP_1 = pygame.K_KP_1
    KP_2 = pygame.K_KP_2
    KP_3 = pygame.K_KP_3
    KP_4 = pygame.K_KP_4
    KP_5 = pygame.K_KP_5
    KP_6 = pygame.K_KP_6
    KP_7 = pygame.K_KP_7
    KP_8 = pygame.K_KP_8
    KP_9 = pygame.K_KP_9
    KP_DIVIDE = pygame.K_KP_DIVIDE
    KP_ENTER = pygame.K_KP_ENTER
    KP_EQUALS = pygame.K_KP_EQUALS
    KP_MINUS = pygame.K_KP_MINUS
    KP_MULTIPLY = pygame.K_KP_MULTIPLY
    KP_PERIOD = pygame.K_KP_PERIOD
    KP_PLUS = pygame.K_KP_PLUS
    L = pygame.K_l
    L_ALT = pygame.K_LALT
    L_CTRL = pygame.K_LCTRL
    LEFT = pygame.K_LEFT
    LEFT_BRACKET = pygame.K_LEFTBRACKET
    LEFT_PAREN = pygame.K_LEFTPAREN
    LESS = pygame.K_LESS
    L_GUI = pygame.K_LGUI
    L_META = pygame.K_LMETA
    L_SHIFT = pygame.K_LSHIFT
    L_SUPER = pygame.K_LSUPER
    M = pygame.K_m
    MENU = pygame.K_MENU
    MINUS = pygame.K_MINUS
    MODE = pygame.K_MODE
    N = pygame.K_n
    NUM_LOCK = pygame.K_NUMLOCK
    NUM_LOCK_CLEAR = pygame.K_NUMLOCKCLEAR
    O = pygame.K_o
    P = pygame.K_p
    PAGEDOWN = pygame.K_PAGEDOWN
    PAGEUP = pygame.K_PAGEUP
    PAUSE = pygame.K_PAUSE
    PERCENT = pygame.K_PERCENT
    PERIOD = pygame.K_PERIOD
    PLUS = pygame.K_PLUS
    POWER = pygame.K_POWER
    PRINT = pygame.K_PRINT
    PRINT_SCREEN = pygame.K_PRINTSCREEN
    Q = pygame.K_q
    QUESTION = pygame.K_QUESTION
    QUOTE = pygame.K_QUOTE
    QUOTE_DBL = pygame.K_QUOTEDBL
    R = pygame.K_r
    R_ALT = pygame.K_RALT
    R_CTRL = pygame.K_RCTRL
    RETURN = pygame.K_RETURN
    R_GUI = pygame.K_RGUI
    RIGHT = pygame.K_RIGHT
    RIGHT_BRACKET = pygame.K_RIGHTBRACKET
    RIGHT_PAREN = pygame.K_RIGHTPAREN
    R_META = pygame.K_RMETA
    R_SHIFT = pygame.K_RSHIFT
    R_SUPER = pygame.K_RSUPER
    S = pygame.K_s
    SCROLL_LOCK = pygame.K_SCROLLLOCK
    SEMICOLON = pygame.K_SEMICOLON
    SLASH = pygame.K_SLASH
    SPACE = pygame.K_SPACE
    SYS_REQ = pygame.K_SYSREQ
    T = pygame.K_t
    TAB = pygame.K_TAB
    U = pygame.K_u
    UNDERSCORE = pygame.K_UNDERSCORE
    UNKNOWN = pygame.K_UNKNOWN
    UP = pygame.K_UP
    V = pygame.K_v
    W = pygame.K_w
    X = pygame.K_x
    Y = pygame.K_y
    Z = pygame.K_z


class KeyScan(Enum):
    INVALID = -1
    N0 = pygame.KSCAN_0
    N1 = pygame.KSCAN_1
    N2 = pygame.KSCAN_2
    N3 = pygame.KSCAN_3
    N4 = pygame.KSCAN_4
    N5 = pygame.KSCAN_5
    N6 = pygame.KSCAN_6
    N7 = pygame.KSCAN_7
    N8 = pygame.KSCAN_8
    N9 = pygame.KSCAN_9
    A = pygame.KSCAN_A
    AC_BACK = pygame.KSCAN_AC_BACK
    APOSTROPHE = pygame.KSCAN_APOSTROPHE
    B = pygame.KSCAN_B
    BACKSLASH = pygame.KSCAN_BACKSLASH
    BACKSPACE = pygame.KSCAN_BACKSPACE
    BREAK = pygame.KSCAN_BREAK
    C = pygame.KSCAN_C
    CAPSLOCK = pygame.KSCAN_CAPSLOCK
    CLEAR = pygame.KSCAN_CLEAR
    COMMA = pygame.KSCAN_COMMA
    CURRENCY_SUBUNIT = pygame.KSCAN_CURRENCYSUBUNIT
    CURRENCY_UNIT = pygame.KSCAN_CURRENCYUNIT
    D = pygame.KSCAN_D
    DELETE = pygame.KSCAN_DELETE
    DOWN = pygame.KSCAN_DOWN
    E = pygame.KSCAN_E
    END = pygame.KSCAN_END
    EQUALS = pygame.KSCAN_EQUALS
    ESCAPE = pygame.KSCAN_ESCAPE
    EURO = pygame.KSCAN_EURO
    F = pygame.KSCAN_F
    F1 = pygame.KSCAN_F1
    F10 = pygame.KSCAN_F10
    F11 = pygame.KSCAN_F11
    F12 = pygame.KSCAN_F12
    F13 = pygame.KSCAN_F13
    F14 = pygame.KSCAN_F14
    F15 = pygame.KSCAN_F15
    F2 = pygame.KSCAN_F2
    F3 = pygame.KSCAN_F3
    F4 = pygame.KSCAN_F4
    F5 = pygame.KSCAN_F5
    F6 = pygame.KSCAN_F6
    F7 = pygame.KSCAN_F7
    F8 = pygame.KSCAN_F8
    F9 = pygame.KSCAN_F9
    G = pygame.KSCAN_G
    GRAVE = pygame.KSCAN_GRAVE
    H = pygame.KSCAN_H
    HELP = pygame.KSCAN_HELP
    HOME = pygame.KSCAN_HOME
    I = pygame.KSCAN_I
    INSERT = pygame.KSCAN_INSERT
    INTERNATIONAL1 = pygame.KSCAN_INTERNATIONAL1
    INTERNATIONAL2 = pygame.KSCAN_INTERNATIONAL2
    INTERNATIONAL3 = pygame.KSCAN_INTERNATIONAL3
    INTERNATIONAL4 = pygame.KSCAN_INTERNATIONAL4
    INTERNATIONAL5 = pygame.KSCAN_INTERNATIONAL5
    INTERNATIONAL6 = pygame.KSCAN_INTERNATIONAL6
    INTERNATIONAL7 = pygame.KSCAN_INTERNATIONAL7
    INTERNATIONAL8 = pygame.KSCAN_INTERNATIONAL8
    INTERNATIONAL9 = pygame.KSCAN_INTERNATIONAL9
    J = pygame.KSCAN_J
    K = pygame.KSCAN_K
    KP0 = pygame.KSCAN_KP0
    KP1 = pygame.KSCAN_KP1
    KP2 = pygame.KSCAN_KP2
    KP3 = pygame.KSCAN_KP3
    KP4 = pygame.KSCAN_KP4
    KP5 = pygame.KSCAN_KP5
    KP6 = pygame.KSCAN_KP6
    KP7 = pygame.KSCAN_KP7
    KP8 = pygame.KSCAN_KP8
    KP9 = pygame.KSCAN_KP9
    KP_0 = pygame.KSCAN_KP_0
    KP_1 = pygame.KSCAN_KP_1
    KP_2 = pygame.KSCAN_KP_2
    KP_3 = pygame.KSCAN_KP_3
    KP_4 = pygame.KSCAN_KP_4
    KP_5 = pygame.KSCAN_KP_5
    KP_6 = pygame.KSCAN_KP_6
    KP_7 = pygame.KSCAN_KP_7
    KP_8 = pygame.KSCAN_KP_8
    KP_9 = pygame.KSCAN_KP_9
    KP_DIVIDE = pygame.KSCAN_KP_DIVIDE
    KP_ENTER = pygame.KSCAN_KP_ENTER
    KP_EQUALS = pygame.KSCAN_KP_EQUALS
    KP_MINUS = pygame.KSCAN_KP_MINUS
    KP_MULTIPLY = pygame.KSCAN_KP_MULTIPLY
    KP_PERIOD = pygame.KSCAN_KP_PERIOD
    KP_PLUS = pygame.KSCAN_KP_PLUS
    L = pygame.KSCAN_L
    L_ALT = pygame.KSCAN_LALT
    LANG1 = pygame.KSCAN_LANG1
    LANG2 = pygame.KSCAN_LANG2
    LANG3 = pygame.KSCAN_LANG3
    LANG4 = pygame.KSCAN_LANG4
    LANG5 = pygame.KSCAN_LANG5
    LANG6 = pygame.KSCAN_LANG6
    LANG7 = pygame.KSCAN_LANG7
    LANG8 = pygame.KSCAN_LANG8
    LANG9 = pygame.KSCAN_LANG9
    L_CTRL = pygame.KSCAN_LCTRL
    LEFT = pygame.KSCAN_LEFT
    LEFT_BRACKET = pygame.KSCAN_LEFTBRACKET
    L_GUI = pygame.KSCAN_LGUI
    L_META = pygame.KSCAN_LMETA
    L_SHIFT = pygame.KSCAN_LSHIFT
    L_SUPER = pygame.KSCAN_LSUPER
    M = pygame.KSCAN_M
    MENU = pygame.KSCAN_MENU
    MINUS = pygame.KSCAN_MINUS
    MODE = pygame.KSCAN_MODE
    N = pygame.KSCAN_N
    NON_US_BACKSLASH = pygame.KSCAN_NONUSBACKSLASH
    NON_US_HASH = pygame.KSCAN_NONUSHASH
    NUM_LOCK = pygame.KSCAN_NUMLOCK
    NUM_LOCK_CLEAR = pygame.KSCAN_NUMLOCKCLEAR
    O = pygame.KSCAN_O
    P = pygame.KSCAN_P
    PAGEDOWN = pygame.KSCAN_PAGEDOWN
    PAGEUP = pygame.KSCAN_PAGEUP
    PAUSE = pygame.KSCAN_PAUSE
    PERIOD = pygame.KSCAN_PERIOD
    POWER = pygame.KSCAN_POWER
    PRINT = pygame.KSCAN_PRINT
    PRINT_SCREEN = pygame.KSCAN_PRINTSCREEN
    Q = pygame.KSCAN_Q
    R = pygame.KSCAN_R
    R_ALT = pygame.KSCAN_RALT
    R_CTRL = pygame.KSCAN_RCTRL
    RETURN = pygame.KSCAN_RETURN
    R_GUI = pygame.KSCAN_RGUI
    RIGHT = pygame.KSCAN_RIGHT
    RIGHT_BRACKET = pygame.KSCAN_RIGHTBRACKET
    R_META = pygame.KSCAN_RMETA
    R_SHIFT = pygame.KSCAN_RSHIFT
    R_SUPER = pygame.KSCAN_RSUPER
    S = pygame.KSCAN_S
    SCROLL_LOCK = pygame.KSCAN_SCROLLLOCK
    SEMICOLON = pygame.KSCAN_SEMICOLON
    SLASH = pygame.KSCAN_SLASH
    SPACE = pygame.KSCAN_SPACE
    SYS_REQ = pygame.KSCAN_SYSREQ
    T = pygame.KSCAN_T
    TAB = pygame.KSCAN_TAB
    U = pygame.KSCAN_U
    UNKNOWN = pygame.KSCAN_UNKNOWN
    UP = pygame.KSCAN_UP
    V = pygame.KSCAN_V
    W = pygame.KSCAN_W
    X = pygame.KSCAN_X
    Y = pygame.KSCAN_Y
    Z = pygame.KSCAN_Z


class KeyMod(Enum):
    NONE = pygame.KMOD_NONE  # no modifier keys pressed
    L_SHIFT = pygame.KMOD_LSHIFT  # left shift
    R_SHIFT = pygame.KMOD_RSHIFT  # right shift
    SHIFT = pygame.KMOD_SHIFT  # left shift or right shift or both
    L_CTRL = pygame.KMOD_LCTRL  # left control
    R_CTRL = pygame.KMOD_RCTRL  # right control
    CTRL = pygame.KMOD_CTRL  # left control or right control or both
    L_ALT = pygame.KMOD_LALT  # left alt
    R_ALT = pygame.KMOD_RALT  # right alt
    ALT = pygame.KMOD_ALT  # left alt or right alt or both
    L_META = pygame.KMOD_LMETA  # left meta
    R_META = pygame.KMOD_RMETA  # right meta
    META = pygame.KMOD_META  # left meta or right meta or both
    CAPS = pygame.KMOD_CAPS  # caps lock
    NUM = pygame.KMOD_NUM  # num lock
    ALT_GR = pygame.KMOD_MODE  # AltGr

    def __or__(self, other: Self | int) -> int:
        return self.value | (other if type(other) is int else other.value)

    def __ror__(self, other: Self | int) -> int:
        return self.value | (other if type(other) is int else other.value)

    def __and__(self, other: int) -> int:
        return self.value & other

    def __rand__(self, other: int) -> int:
        return self.value & other


class KeyEvent:
    type: Literal[EventType.KEY_UP, EventType.KEY_DOWN]
    """
    Either EventType.KEY_UP or EventType.KEY_DOWN
    """

    key: Key
    """
    Key that was pressed
    """

    key_code: int
    """
    Code of the key that was pressed
    """

    mods: list[KeyMod]
    """
    All the modifiers that were pressed
    """

    unicode: str | int
    """
    16-bit unicode value of the key
    """

    scancode: KeyScan
    """
    The physical location of a key
    """

    scancode_code: int
    """
    The code of the physical location of a key
    """

    def __init__(self, event: pygame.event.Event):
        self.type = EventType(event.type)

        try:
            self.key = Key(event.key)
        except ValueError:
            self.key = Key.INVALID

        self.key_code = event.key
        self.mods = []
        for mod in list(KeyMod):
            if event.mod & mod != 0:
                self.mods.append(mod)

        self.unicode = event.unicode

        try:
            self.scancode = KeyScan(event.scancode)
        except ValueError:
            self.scancode = KeyScan.INVALID

        self.scancode_code = event.scancode

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
