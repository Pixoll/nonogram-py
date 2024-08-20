import pygame

from typing import Literal, Self
from enum import Enum
from src.events.event_type import EventType


class Key(Enum):
    BACKSPACE = pygame.K_BACKSPACE  # \b backspace
    TAB = pygame.K_TAB  # \t tab
    CLEAR = pygame.K_CLEAR  # clear
    RETURN = pygame.K_RETURN  # \r return
    PAUSE = pygame.K_PAUSE  # pause
    ESCAPE = pygame.K_ESCAPE  # ^[ escape
    SPACE = pygame.K_SPACE  # space
    EXCLAIM = pygame.K_EXCLAIM  # ! exclaim
    QUOTE_DBL = pygame.K_QUOTEDBL  # " quotedbl
    HASH = pygame.K_HASH  # (#) hash
    DOLLAR = pygame.K_DOLLAR  # $ dollar
    AMPERSAND = pygame.K_AMPERSAND  # & ampersand
    QUOTE = pygame.K_QUOTE  # quote
    LEFT_PAREN = pygame.K_LEFTPAREN  # ( left parenthesis
    RIGHT_PAREN = pygame.K_RIGHTPAREN  # ) right parenthesis
    ASTERISK = pygame.K_ASTERISK  # * asterisk
    PLUS = pygame.K_PLUS  # + plus sign
    COMMA = pygame.K_COMMA  # , comma
    MINUS = pygame.K_MINUS  # - minus sign
    PERIOD = pygame.K_PERIOD  # . period
    SLASH = pygame.K_SLASH  # / forward slash
    K0 = pygame.K_0  # 0
    K1 = pygame.K_1  # 1
    K2 = pygame.K_2  # 2
    K3 = pygame.K_3  # 3
    K4 = pygame.K_4  # 4
    K5 = pygame.K_5  # 5
    K6 = pygame.K_6  # 6
    K7 = pygame.K_7  # 7
    K8 = pygame.K_8  # 8
    K9 = pygame.K_9  # 9
    COLON = pygame.K_COLON  # : colon
    SEMICOLON = pygame.K_SEMICOLON  # ; semicolon
    LESS = pygame.K_LESS  # < less-than sign
    EQUALS = pygame.K_EQUALS  # = equals sign
    GREATER = pygame.K_GREATER  # > greater-than sign
    QUESTION = pygame.K_QUESTION  # ? question mark
    AT = pygame.K_AT  # @ at
    LEFT_BRACKET = pygame.K_LEFTBRACKET  # [ left bracket
    BACKSLASH = pygame.K_BACKSLASH  # \ backslash
    RIGHT_BRACKET = pygame.K_RIGHTBRACKET  # ]right bracket
    CARET = pygame.K_CARET  # ^ caret
    UNDERSCORE = pygame.K_UNDERSCORE  # _ underscore
    BACKQUOTE = pygame.K_BACKQUOTE  # ` grave
    a = pygame.K_a  # a
    b = pygame.K_b  # b
    c = pygame.K_c  # c
    d = pygame.K_d  # d
    e = pygame.K_e  # e
    f = pygame.K_f  # f
    g = pygame.K_g  # g
    h = pygame.K_h  # h
    i = pygame.K_i  # i
    j = pygame.K_j  # j
    k = pygame.K_k  # k
    l = pygame.K_l  # l
    m = pygame.K_m  # m
    n = pygame.K_n  # n
    o = pygame.K_o  # o
    p = pygame.K_p  # p
    q = pygame.K_q  # q
    r = pygame.K_r  # r
    s = pygame.K_s  # s
    t = pygame.K_t  # t
    u = pygame.K_u  # u
    v = pygame.K_v  # v
    w = pygame.K_w  # w
    x = pygame.K_x  # x
    y = pygame.K_y  # y
    z = pygame.K_z  # z
    DELETE = pygame.K_DELETE  # delete
    KP0 = pygame.K_KP0  # keypad 0
    KP1 = pygame.K_KP1  # keypad 1
    KP2 = pygame.K_KP2  # keypad 2
    KP3 = pygame.K_KP3  # keypad 3
    KP4 = pygame.K_KP4  # keypad 4
    KP5 = pygame.K_KP5  # keypad 5
    KP6 = pygame.K_KP6  # keypad 6
    KP7 = pygame.K_KP7  # keypad 7
    KP8 = pygame.K_KP8  # keypad 8
    KP9 = pygame.K_KP9  # keypad 9
    KP_PERIOD = pygame.K_KP_PERIOD  # . keypad period
    KP_DIVIDE = pygame.K_KP_DIVIDE  # / keypad divide
    KP_MULTIPLY = pygame.K_KP_MULTIPLY  # * keypad multiply
    KP_MINUS = pygame.K_KP_MINUS  # - keypad minus
    KP_PLUS = pygame.K_KP_PLUS  # + keypad plus
    KP_ENTER = pygame.K_KP_ENTER  # \r keypad enter
    KP_EQUALS = pygame.K_KP_EQUALS  # = keypad equals
    UP = pygame.K_UP  # up arrow
    DOWN = pygame.K_DOWN  # down arrow
    RIGHT = pygame.K_RIGHT  # right arrow
    LEFT = pygame.K_LEFT  # left arrow
    INSERT = pygame.K_INSERT  # insert
    HOME = pygame.K_HOME  # home
    END = pygame.K_END  # end
    PAGEUP = pygame.K_PAGEUP  # page up
    PAGEDOWN = pygame.K_PAGEDOWN  # page down
    F1 = pygame.K_F1  # F1
    F2 = pygame.K_F2  # F2
    F3 = pygame.K_F3  # F3
    F4 = pygame.K_F4  # F4
    F5 = pygame.K_F5  # F5
    F6 = pygame.K_F6  # F6
    F7 = pygame.K_F7  # F7
    F8 = pygame.K_F8  # F8
    F9 = pygame.K_F9  # F9
    F10 = pygame.K_F10  # F10
    F11 = pygame.K_F11  # F11
    F12 = pygame.K_F12  # F12
    F13 = pygame.K_F13  # F13
    F14 = pygame.K_F14  # F14
    F15 = pygame.K_F15  # F15
    NUMLOCK = pygame.K_NUMLOCK  # numlock
    CAPSLOCK = pygame.K_CAPSLOCK  # capslock
    SCROLLOCK = pygame.K_SCROLLOCK  # scrollock
    RSHIFT = pygame.K_RSHIFT  # right shift
    LSHIFT = pygame.K_LSHIFT  # left shift
    RCTRL = pygame.K_RCTRL  # right control
    LCTRL = pygame.K_LCTRL  # left control
    RALT = pygame.K_RALT  # right alt
    LALT = pygame.K_LALT  # left alt
    RMETA = pygame.K_RMETA  # right meta
    LMETA = pygame.K_LMETA  # left meta
    LSUPER = pygame.K_LSUPER  # left Windows key
    RSUPER = pygame.K_RSUPER  # right Windows key
    MODE = pygame.K_MODE  # mode shift
    HELP = pygame.K_HELP  # help
    PRINT = pygame.K_PRINT  # print screen
    SYSREQ = pygame.K_SYSREQ  # sysrq
    BREAK = pygame.K_BREAK  # break
    MENU = pygame.K_MENU  # menu
    POWER = pygame.K_POWER  # power
    EURO = pygame.K_EURO  # Euro
    AC_BACK = pygame.K_AC_BACK  # Android back button


class KeyMod(Enum):
    NONE = pygame.KMOD_NONE  # no modifier keys pressed
    LSHIFT = pygame.KMOD_LSHIFT  # left shift
    RSHIFT = pygame.KMOD_RSHIFT  # right shift
    SHIFT = pygame.KMOD_SHIFT  # left shift or right shift or both
    LCTRL = pygame.KMOD_LCTRL  # left control
    RCTRL = pygame.KMOD_RCTRL  # right control
    CTRL = pygame.KMOD_CTRL  # left control or right control or both
    LALT = pygame.KMOD_LALT  # left alt
    RALT = pygame.KMOD_RALT  # right alt
    ALT = pygame.KMOD_ALT  # left alt or right alt or both
    LMETA = pygame.KMOD_LMETA  # left meta
    RMETA = pygame.KMOD_RMETA  # right meta
    META = pygame.KMOD_META  # left meta or right meta or both
    CAPS = pygame.KMOD_CAPS  # caps lock
    NUM = pygame.KMOD_NUM  # num lock
    ALTGR = pygame.KMOD_MODE  # AltGr

    def __or__(self, other: Self | int) -> int:
        return self.value | (other if type(other) is int else other.value)

    def __and__(self, other: int) -> int:
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

    mod: int
    """
    Obtained from OR-ing with different KeyMods
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
        self.mod = event.mod
        self.unicode = event.unicode
        self.scancode = event.scancode

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.__dict__}>  "
