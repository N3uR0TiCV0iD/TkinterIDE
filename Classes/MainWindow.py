from tkinter import *
from MainWindow_Designer import *

CURSOR_TOOL = 0
BUTTON_TOOL = 1
FRAME_TOOL = 2

class MainWindow:
    def __init__(self):
        initWindow(self)
        self.lastWindowX = self.window.winfo_x()
        self.lastWindowY = self.window.winfo_y()
        self.lastWindowWidth = self.window.winfo_width()
        self.lastWindowHeight = self.window.winfo_height()
    #end function

    def cursorTool_Click(self):
        self.selectedTool = CURSOR_TOOL
        print("Selected: CursorTool")
    #end function
    def buttonTool_Click(self):
        self.selectedTool = BUTTON_TOOL
        print("Selected: ButtonTool")
    #end function
    def frameTool_Click(self):
        self.selectedTool = FRAME_TOOL
        print("Selected: FrameTool")
    #end function

    def designHandler_Click(self, event):
        if self.selectedTool == CURSOR_TOOL:
            print("SELECT WIDGET!")
        else:
            #Check if the user clicked on a container and insert it in said container! (e.g. a frame)
            if self.selectedTool == BUTTON_TOOL:
                newWidget = Button(self.designWindow, text="Button")
            elif self.selectedTool == FRAME_TOOL:
                newWidget = Frame(self.designWindow, relief=GROOVE)
                newWidget.place(width=200, height=100)
            #end if
            newWidget.place(x=event.x, y=event.y)
            self.editTabs.windows[0].widgets.append(newWidget)
            self.cursorTool_Click()
        #end if
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
        self.updateDesignWindow()
    #end function
    def updateDesignWindow(self):
        currWindowX = self.window.winfo_x()
        currWindowY = self.window.winfo_y()
        designWindowPos = "+" + str(currWindowX + self.mainPanes.sashpos(0) + 25) + "+" + str(currWindowY + 65)
        self.designHandler.geometry(designWindowPos)
        self.designWindow.geometry(designWindowPos)
        #self.designWindow.geometry(str(self.mainPanes.sashpos(1) - self.mainPanes.sashpos(0) - 45) +
        #                     "x" + str(self.viewPanes.sashpos(0) - 85) +
        #                     "+" + str(currWindowX + self.mainPanes.sashpos(0) + 25) +
        #                     "+" + str(currWindowY + 65))
        self.lastWindowX = currWindowX
        self.lastWindowY = currWindowX
    #end function
    def show(self):
        self.window.mainloop()
    #end function
#end class
