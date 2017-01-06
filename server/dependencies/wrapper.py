# NOTE: tkinter has a lot of inconsistencies within its design, as well as a lot of unnecessary boilerplate code.
# This class is meant to fix those issues, and is not directly related to my project

from tkinter import Frame as tkFrame
from enum import Enum, auto
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
    ARROW = auto()
    MAN = auto()
    BASED_ARROW_DOWN = auto()
    MIDDLEBUTTON = auto()
    BASED_ARROW_UP = auto()
    MOUSE = auto()
    BOAT = auto()
    PENCIL = auto()
    BOGOSITY = auto()
    PIRATE = auto()
    BOTTOM_LEFT_CORNER = auto()
    PLUS = auto()
    BOTTOM_RIGHT_CORNER = auto()
    QUESTION_ARROW = auto()
    BOTTOM_SIDE = auto()
    RIGHT_PTR = auto()
    BOTTOM_TEE = auto()
    RIGHT_SIDE = auto()
    BOX_SPIRAL = auto()
    RIGHT_TEE = auto()
    CENTER_PTR = auto()
    RIGHTBUTTON = auto()
    CIRCLE = auto()
    RTL_LOGO = auto()
    CLOCK = auto()
    SAILBOAT = auto()
    COFFEE_MUG = auto()
    SB_DOWN_ARROW = auto()
    CROSS = auto()
    SB_H_DOUBLE_ARROW = auto()
    CROSS_REVERSE = auto()
    SB_LEFT_ARROW = auto()
    CROSSHAIR = auto()
    SB_RIGHT_ARROW = auto()
    DIAMOND_CROSS = auto()
    SB_UP_ARROW = auto()
    DOT = auto()
    SB_V_DOUBLE_ARROW = auto()
    DOTBOX = auto()
    SHUTTLE = auto()
    DOUBLE_ARROW = auto()
    SIZING = auto()
    DRAFT_LARGE = auto()
    SPIDER = auto()
    DRAFT_SMALL = auto()
    SPRAYCAN = auto()
    DRAPED_BOX = auto()
    STAR = auto()
    EXCHANGE = auto()
    TARGET = auto()
    FLEUR = auto()
    TCROSS = auto()
    GOBBLER = auto()
    TOP_LEFT_ARROW = auto()
    GUMBY = auto()
    TOP_LEFT_CORNER = auto()
    HAND1 = auto()
    TOP_RIGHT_CORNER = auto()
    HAND2 = auto()
    TOP_SIDE = auto()
    HEART = auto()
    TOP_TEE = auto()
    ICON = auto()
    TREK = auto()
    IRON_CROSS = auto()
    UL_ANGLE = auto()
    LEFT_PTR = auto()
    UMBRELLA = auto()
    LEFT_SIDE = auto()
    UR_ANGLE = auto()
    LEFT_TEE = auto()
    WATCH = auto()
    LEFTBUTTON = auto()
    XTERM = auto()
    LL_ANGLE = auto()
    X_CURSOR = auto()
    LR_ANGLE = auto()

# tkinter's way of handling fonts is extremely cumbersome and the implementation is not consistent.
# This class is designed to fix both of these issues
class Font():
    def __init__(self):
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

        self.font = tkFont.Font(family=self.family, size=self.size, weight=tkBold, slant=tkItalic, underline=self.underline, overstrike=self.overstrike)



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
        self.config(cursor=str.lower(cursor.name))

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
        self.config(font=self.font.font)

    def bold(self, bool):
        self.font.bold = bool
        self.font.update()
        self.config(font=self.font.font)

    def underline(self, bool):
        self.font.underline = bool
        self.font.update()
        self.config(font=self.font.font)
