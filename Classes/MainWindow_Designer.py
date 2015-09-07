from tkinter import *
from tkinter.ttk import *
from DesignWindowData import *

def initWindow(self):
    #self.window
    self.window = Tk()
    self.window.bind("<Configure>", self.window_Resize)
    self.window.geometry("800x600+50+50")
    self.window.title("Tkinter IDE")
    self.window.minsize(535, 400)

    self.designWindow = Toplevel(self.window)
    self.designWindow.wm_attributes("-disabled", 1)
    self.designWindow.transient(self.window)
    self.designWindow.title("MainWindow")
    self.designWindow.geometry("300x300")

    self.designHandler = Toplevel(self.window)
    self.designHandler.bind("<Button-1>", self.designHandler_Click)
    self.designHandler.wm_attributes("-alpha", 0.01)
    self.designHandler.transient(self.window)
    self.designHandler.geometry("300x300")

    #http://www.tkdocs.com/tutorial/windows.html

    self.mainPanes = PanedWindow(self.window, orient=HORIZONTAL)
    self.mainPanes.pack(fill=BOTH, expand=1)

    self.toolBox = Frame(self.mainPanes, relief=GROOVE)

    self.buttonTool = Button(self.toolBox, text="Cursor", command=self.cursorTool_Click)
    self.buttonTool.place(x=10, y=10, width=100, height=23)

    self.buttonTool = Button(self.toolBox, text="Button", command=self.buttonTool_Click)
    self.buttonTool.place(x=10, y=40, width=100, height=23)

    self.frameTool = Button(self.toolBox, text="Frame", command=self.frameTool_Click)
    self.frameTool.place(x=10, y=70, width=100, height=23)

    self.viewPanes = PanedWindow(self.mainPanes, orient=VERTICAL) #Code/Design View & Console View

    self.editTabs = Notebook(self.viewPanes)
    self.editTabs.windows = []
    self.editTabs.windows.append(DesignWindowData(self.editTabs))
    self.editTabs.add(self.editTabs.windows[0].design, text='MainWindow.py [Design]')
    self.editTabs.add(self.editTabs.windows[0].code, text='MainWindow.py')
    self.editTabs.windows[0].widgets = []

    self.consoleBox = Text(self.viewPanes)

    self.selectionPanes = PanedWindow(self.mainPanes, orient=VERTICAL)

    self.projectView = Treeview(self.selectionPanes)

    self.propertiesBox = Frame(self.selectionPanes, relief=GROOVE)

    self.mainPanes.add(self.toolBox)
    self.mainPanes.add(self.viewPanes)
    self.mainPanes.add(self.selectionPanes)
    self.mainPanes.update()
    self.mainPanes.sashpos(0, 125)
    self.mainPanes.sashpos(1, 650)

    self.viewPanes.add(self.editTabs)
    self.viewPanes.add(self.consoleBox)
    self.viewPanes.update()
    self.viewPanes.sashpos(0, 450)

    self.selectionPanes.add(self.projectView)
    self.selectionPanes.add(self.propertiesBox)
    self.selectionPanes.update()
    self.selectionPanes.sashpos(0, 250)

#end function
