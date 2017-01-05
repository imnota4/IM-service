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
        self.resize(640, 480)
        self.cursor(Cursors.BOAT)
        self.config(highlightbackground="#58f210")

    def createWindow(self):
        self.textWindow = TextMenu(self)
        self.onlineWindow = Frame(self)
        self.inputWindow = Text(self)
        self.textWindow.config(borderwidth=2)
        self.inputWindow.config(background="#d8d8d8", borderwidth=2)
        self.onlineWindow.config(background="#d8d8d8", borderwidth=2)
        self.textWindow.place(relx=0, rely=0, relheight=.8, relwidth=.75)
        self.inputWindow.place(relx=0, rely=.8, relheight=.2, relwidth=1)
        self.onlineWindow.place(relx=.75, rely=0, relwidth=.25, relheight=.8)


    def startLoop(self):
        self.mainWindow.mainloop()


mainWindow = ServerWindow()
mainWindow.mainloop()