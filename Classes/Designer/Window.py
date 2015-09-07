from tkinter import *
from tkinter.ttk import *
from threading import Thread

class Window:
    def __init__(self):
        self.window = Tk()
    #end contructor
    def show(self):
        windowThread = Thread(self.window.mainloop, None)
        windowThread.start()
    #end function
#end class
