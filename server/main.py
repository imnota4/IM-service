from dependencies.wrapper import FrameWrapper as Frame
from tkinter import Tk as Tk
from tkinter import Text as Text
from dependencies.wrapper import CursorStyle as Cursors



class TextMenu(Frame):
    def __init__(self, master):
        super().__init__(master)

    def addText(self):
        pass

    def deleteText(self):
        pass    


class ServerWindow(Frame):
    def __init__(self):
        self.mainWindow = Tk()
        super().__init__(self.mainWindow)
        self.grid()
        self.createWindow()
        self.absSize(640, 640)
        self.cursor(Cursors.BOAT)

    def createWindow(self):
        self.textWindow = Frame(self)
        self.textWindow.relPos(0, 0)
        self.textWindow.relSize(.75, .80)
        self.textWindow.highlightThickness(2)
        self.textWindow.unfocusHightlight(255, 255, 255)
        self.textWindow.focusHighlight(255, 255, 255)

        self.onlineWindow = Frame(self)
        self.onlineWindow.borderSize(2)
        self.onlineWindow.relPos(.75, 0)
        self.onlineWindow.relSize(.25, .8)
        self.onlineWindow.highlightThickness(2)
        self.onlineWindow.unfocusHightlight(255, 255, 255)
        self.onlineWindow.focusHighlight(255, 255, 255)

        self.inputWindow = Frame(self)
        self.inputWindow.borderSize(2)
        self.inputWindow.relPos(0, .8)
        self.inputWindow.relSize(1, .2)
        self.inputWindow.highlightThickness(2)
        self.inputWindow.unfocusHightlight(255, 255, 255)
        self.inputWindow.focusHighlight(255, 255, 255)



    def startLoop(self):
        self.mainWindow.mainloop()


mainWindow = ServerWindow()
mainWindow.mainloop()