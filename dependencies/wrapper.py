# NOTE: tkinter has a lot of inconsistencies within its design, as well as a lot of unnecessary boilerplate code.
# This class is meant to fix those issues, and is not directly related to my project

from tkinter import Frame as tkFrame
import tkinter
from enum import Enum
from tkinter import FLAT as tkFlat
from tkinter import RAISED as tkRaised
from tkinter import GROOVE as tkGroove
from tkinter import SUNKEN as tkSunken
from tkinter import RIDGE as tkRidge
from tkinter import Label as tkLabel
from tkinter import font as tkFont

# This class is designed to separate the enums from the package itself so importing is easier
class BorderStyles(Enum):
    FLAT = tkFlat
    RAISED = tkRaised
    GROOVE = tkGroove
    SUNKEN = tkSunken
    RIDGE = tkRidge

# Cursor styles are not Enums initially. This class makes Enums for the different styles, for simplicity as well as documentation purposes.
# The values have no meaning. They exist only because it is required.
class CursorStyle(Enum):
    ARROW = "arrow"
    MAN = "man"
    BASED_ARROW_DOWN = "based_arrow_down"
    MIDDLEBUTTON = "middlebutton"
    BASED_ARROW_UP = "based_arrow_up"
    MOUSE = "mouse"
    BOAT = "boat"
    PENCIL = "pencil"
    BOGOSITY = "bogosity"
    PIRATE = "pirate"
    BOTTOM_LEFT_CORNER = "bottom_left_corner"
    PLUS = "plus"
    BOTTOM_RIGHT_CORNER = "bottom_right_corner"
    QUESTION_ARROW = "question_arrow"
    BOTTOM_SIDE = "bottom_side"
    RIGHT_PTR = "right_ptr"
    BOTTOM_TEE = "bottom_tee"
    RIGHT_SIDE = "right_side"
    BOX_SPIRAL = "box_spiral"
    RIGHT_TEE = "right_tee"
    CENTER_PTR = "center_ptr"
    RIGHTBUTTON = "rightbutton"
    CIRCLE = "circle"
    RTL_LOGO = "rtl_logo"
    CLOCK = "clock"
    SAILBOAT = "sailboat"
    COFFEE_MUG = "coffee_mug"
    SB_DOWN_ARROW = "sb_down_arrow"
    CROSS = "cross"
    SB_H_DOUBLE_ARROW = "sb_h_double_arrow"
    CROSS_REVERSE = "cross_reverse"
    SB_LEFT_ARROW = "sb_left_arrow"
    CROSSHAIR = "crosshair"
    SB_RIGHT_ARROW = "sb_right_arrow"
    DIAMOND_CROSS = "diamond_cross"
    SB_UP_ARROW = "sb_up_arrow"
    DOT = "dot"
    SB_V_DOUBLE_ARROW = "sb_v_double_arrow"
    DOTBOX = "dotbox"
    SHUTTLE = "shuttle"
    DOUBLE_ARROW = "double_arrow"
    SIZING = "sizing"
    DRAFT_LARGE = "draft_large"
    SPIDER = "spider"
    DRAFT_SMALL = "draft_small"
    SPRAYCAN = "spraycan"
    DRAPED_BOX = "draped_box"
    STAR = "star"
    EXCHANGE = "exchange"
    TARGET = "target"
    FLEUR = "fleur"
    TCROSS = "tcross"
    GOBBLER = "gobbler"
    TOP_LEFT_ARROW = "top_left_arrow"
    GUMBY = "gumby"
    TOP_LEFT_CORNER = "top_left_corner"
    HAND1 = "hand1"
    TOP_RIGHT_CORNER = "top_right_corner"
    HAND2 = "hand2"
    TOP_SIDE = "top_side"
    HEART = "heart"
    TOP_TEE = "top_tee"
    ICON = "icon"
    TREK = "trek"
    IRON_CROSS = "iron_cross"
    UL_ANGLE = "ul_angle"
    LEFT_PTR = "left_ptr"
    UMBRELLA = "umbrella"
    LEFT_SIDE = "left_side"
    UR_ANGLE = "ur_angle"
    LEFT_TEE = "left_tee"
    WATCH = "watch"
    LEFTBUTTON = "leftbutton"
    XTERM = "xterm"
    LL_ANGLE = "ll_angle"
    X_CURSOR = "x_cursor"
    LR_ANGLE = "lr_angle"


# tkinter's way of handling fonts is extremely cumbersome and the implementation is not consistent.
# This class is designed to fix both of these issues
class Font(tkFont.Font):
    def __init__(self):
        super().__init__()
        self.family = "Times"
        self.size = 12
        self.bold = False
        self.italic = False
        self.underline = False
        self.overstrike = False
        self.update()

    def update(self):
        tkBold = "normal"
        tkItalic = "roman"

        if self.bold:
            tkBold = "bold"
        if self.italic:
            tkItalic = "italic"

        newFont = tkFont.Font(family=self.family, size=self.size, weight=tkBold, slant=tkItalic, underline=self.underline, overstrike=self.overstrike)
        options = newFont.actual() # Gets a list of the new font's properties. Inherited from font.py
        self._call("font", "config", self.name, *self._set(options)) # replaces current font's properties with the ones located in 'options'. Inherited from font.py


# This class wraps the functionality within the tkinter.Frame class into easier to use functions
class FrameWrapper(tkFrame):
    def __init__(self, master):
        super().__init__(master)

    def relPos(self, posx, posy):
        self.place(relx=posx, rely=posy)

    def relSize(self, width, height):
        self.place(relwidth=width, relheight=height)

    def absPos(self, xpos, ypos):
        self.place(x=xpos, rely=ypos)

    def bgColor(self, r, g, b):
        self.configure(background="#" + str(r) + str(g) + str(b))

    def borderSize(self, size):
        self.config(borderwidth=size)
    # cursor: One of the enums located in CursorStyle class
    def cursor(self, cursor):

        if type(cursor) == CursorStyle: # Required for compatibility with tkinter
            cursor = cursor.value

        self.config(cursor=cursor)

    # Sets the color of the highlighter when window gets keyboard focus. Note: Does not highlight from cursor focus
    def focusHighlight(self, r, g, b):
        self.config(highlightcolor="#" + str(r) + str(g) + str(b))

    # Sets the color of the highlighter when window loses keyboard focus.
    def unfocusHightlight(self, r, g, b):
        self.config(highlightbackground="#" + str(r) + str(g) + str(b))

    def highlightThickness(self, thickness):
        self.config(highlightthickness=thickness)

    def horizontalPadding(self, size):
        self.config(padx=size)

    def verticalPadding(self, size):
        self.config(pady=size)

    def absSize(self, width, height):
        self.configure(width=width, height=height)

    # style: One of the enums located in BorderStyles class
    def borderStyle(self, style):

        if type(style) == BorderStyles: # Required for compatibility with tkinter
            style = style.value

        self.configure(relief=style)

    def allowKeyboardFocus(self, bool):
        self.config(takefocus=bool)

# This class wraps the functionality in the tkinter.Label class into easier to use functions.
# This class does not currently support all functionality within the tkinter.Label class. It will be added when necessary
class Label(tkLabel, FrameWrapper):
    def __init__(self, master, msg):
        super().__init__(master, text=msg)
        self.font = Font()

    def fontSize(self, size):
        self.font.size = size
        self.font.update()
        self.config(font=self.font)

    def bold(self, bool):
        self.font.bold = bool
        self.font.update()
        self.config(font=self.font)

    def underline(self, bool):
        self.font.underline = bool
        self.font.update()
        self.config(font=self.font)
