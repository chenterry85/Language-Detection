from tkinter import Tk
import GUI

root = Tk()
root.minsize(width = 520,height = 395)
root.maxsize(width = 520,height = 395)
root.title("Language Detection")
app = GUI.Application(root)
root.mainloop()
