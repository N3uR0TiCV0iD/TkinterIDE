from tkinter import *
from MainWindow_Designer import *

class MainWindow:
    def __init__(self):
        initWindow(self)
        self.lastWindowWidth = self.window.winfo_width()
        self.lastWindowHeight = self.window.winfo_height()
    #end function
    def okButton_Click(self):
        print("HI!")
    #end function

    def buttonTool_Click(self):
        print("You selected button!")
    #end function
    def panelTool_Click(self):
        print("You selected panel!")
    #end function

    def designWidget_MouseMove(self):
        #, "<B1-Motion>", self.mouseMove)
        print()
    #end function
    def designWidget_MouseEnter(self):
        print()
    #end function
    def window_Resize(self, event):
        currWidth = self.window.winfo_width()
        currHeight = self.window.winfo_height()
        if currWidth == event.width and currHeight == event.height:
            #IsMoving the window!
            editViewSashDiff = self.lastWindowWidth - self.mainPanes.sashpos(1)
            self.mainPanes.sashpos(1, currWidth - editViewSashDiff)

            editViewSashDiff = self.lastWindowHeight - self.viewPanes.sashpos(0)
            self.viewPanes.sashpos(0, currHeight - editViewSashDiff)

            self.lastWindowHeight = currHeight
            self.lastWindowWidth = currWidth
        #end if
    #end function
    def show(self):
        self.window.mainloop()
    #end function
#end class
