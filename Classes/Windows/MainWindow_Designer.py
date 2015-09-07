from tkinter import *
from tkinter.ttk import *

def initWindow(self):
    #self.window
    self.window = Tk()
    self.window.title("Tkinter IDE")
    self.window.geometry("800x600")
    self.window.geometry("+50+50")
    #self.window.minsize(200, 100)
    #self.window.maxsize(500, 500)
    self.window.bind("<Configure>", self.window_Resize)
    #/self.window

    #http://www.tkdocs.com/tutorial/windows.html

    self.mainPanes = PanedWindow(self.window, orient=HORIZONTAL)
    self.mainPanes.pack(fill=BOTH, expand=1)

    self.toolBox = Frame(self.mainPanes, relief=GROOVE)

    self.buttonTool = Button(self.toolBox, text="Button", command=self.okButton_Click)
    self.buttonTool.place(x=10, y=10, width=100, height=23)

    self.panelTool = Button(self.toolBox, text="Pane", command=self.okButton_Click)
    self.panelTool.place(x=10, y=40, width=100, height=23)

    self.viewPanes = PanedWindow(self.mainPanes, orient=VERTICAL) #Code/Design View & Console View

    self.editTabs = Notebook(self.viewPanes)
    self.editTabs.tab1 = Frame(self.editTabs)
    self.editTabs.tab2 = Frame(self.editTabs)
    self.editTabs.add(self.editTabs.tab1, text='MainWindow.py [Design]')
    self.editTabs.add(self.editTabs.tab2, text='MainWindow.py')

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
