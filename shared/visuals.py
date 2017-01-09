from dependencies.wrapper import FrameWrapper as Frame
from tkinter import Tk
from dependencies.wrapper import CursorStyle as Cursors
from dependencies.wrapper import Label

class OnlineUsersList(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.relPos(.75, 0)
        self.relSize(.25, .8)
        self.highlightThickness(2)
        self.unfocusHightlight(255, 255, 255)
        self.focusHighlight(255, 255, 255)
        self.header = Label(self, "Online users")
        self.header.relPos(.18, 0)
        self.header.fontSize(12)
        self.header.bold(True)
        self.header.underline(True)
    def addUser(self):
        pass

    def removeUser(self):
        pass

class UIHandle(Frame):
    def __init__(self):
        self.mainWindow = Tk()
        super().__init__(self.mainWindow)
        self.grid()
        self.createWindow()
        self.absSize(640, 640)
        self.cursor(Cursors.BOAT)
        self.startLoop()

    def createWindow(self):
        self.textWindow = Frame(self)
        self.textWindow.relPos(0, 0)
        self.textWindow.relSize(.75, .80)
        self.textWindow.highlightThickness(2)
        self.textWindow.unfocusHightlight(255, 255, 255)
        self.textWindow.focusHighlight(255, 255, 255)

        self.onlineWindow = OnlineUsersList(self)


        self.inputWindow = Frame(self)
        self.inputWindow.borderSize(2)
        self.inputWindow.relPos(0, .8)
        self.inputWindow.relSize(1, .2)
        self.inputWindow.highlightThickness(2)
        self.inputWindow.unfocusHightlight(255, 255, 255)
        self.inputWindow.focusHighlight(255, 255, 255)

    def startLoop(self):
        self.mainWindow.mainloop()
