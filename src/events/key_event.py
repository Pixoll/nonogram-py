from enum import Enum
from typing import Literal, Self

import pygame

from events.event_type import EventType


class Key(Enum):
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
    type: Literal[EventType.KEY_UP] | Literal[EventType.KEY_DOWN]
    """
    Either EventType.KEY_UP or EventType.KEY_DOWN
    """

    key: Key
    """
    Key that was pressed
    """

    mods: list[KeyMod]
    """
    All the modifiers that were pressed
    """

    unicode: str | int
    """
    16-bit unicode value of the key
    """

    scancode: int
    """
    The physical location of a key
    """

    def __init__(self, event: pygame.event.Event):
        self.type = EventType(event.type)
        self.key = Key(event.key)

        self.mod = []
        for mod in list(KeyMod):
            if event.mod & mod != 0:
                self.mod.append(mod)

        self.unicode = event.unicode
        self.scancode = event.scancode

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>"
