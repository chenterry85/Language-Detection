from tkinter import Tk
import GUI

root = Tk()
root.minsize(width=540,height=330)
root.maxsize(width=540,height=330)
root.title("Language Detection")
app = GUI.Application(root)
root.mainloop()
