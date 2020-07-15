from tkinter import *
import domain

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        domain.init_freq_table()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.data_from_file = True
        self.TEXT_BOX_WIDTH = 50
        self.TEXT_BOX_HEIGHT = 10

        self.l1 = Label(self, text="  Data location: ")
        self.l1.grid(row = 0, column = 0)

        self.chooser = StringVar()
        self.r1 = Radiobutton(self,
                            text="File",
                            variable=self.chooser,
                            value="1",
                            command= self.updateChoice)
        self.r1.grid(row=0, column=1)
        self.r2 = Radiobutton(self,
                            text="Textbox",
                            variable=self.chooser,
                            value="2",
                            command= self.updateChoice)
        self.r2.grid(row=0, column=2)
        self.chooser.set("1")

        self.space2 = Label(self,text="   ")
        self.space2.grid(row = 0, column = 3, rowspan = 5)

        self.l2 = Label(self,text="  Text:")
        self.l2.grid(row=1, column=0,sticky = W)

        self.input = Text(self, width = self.TEXT_BOX_WIDTH, height = self.TEXT_BOX_HEIGHT, wrap = WORD)
        self.input.grid(row=1,column = 1, columnspan=2, sticky = W)

        self.b1 = Button(self,text="Scan", padx = 10, command = self.buttonAction)
        self.b1.grid(row=2,column =2, columnspan = 1)

        self.b2 = Button(self,text="Clear", padx = 10, command = self.clear)
        self.b2.grid(row = 2, column = 2,columnspan = 1, stick = E)

        self.space1 = Label(self, text="")
        self.space1.grid(row = 3,column = 2)

        self.l3 = Label(self, text = "  Language:")
        self.l3.grid(row = 4,column = 0, columnspan = 1, sticky = W)

        self.output = Text(self, width = self.TEXT_BOX_WIDTH, height = 5, wrap = WORD)
        self.output.grid(row=4,column = 1, columnspan=2, sticky = W)
        self.setText("No input")

    def buttonAction(self):

        if self.data_from_file:
            content = domain.get_input_text()
            self.setText(domain.get_language(content))
        else:
            content = self.input.get(1.0,END)
            if not content.rstrip():
                self.setText("No input")
            else:
                self.setText(domain.get_language(content))

    def updateChoice(self):
        self.data_from_file = True if self.chooser.get() == "1" else False

    def setText(self,text):
        self.output.delete(1.0,END)
        self.output.insert(END,text)

    def clear(self):
        self.input.delete(1.0,END)
