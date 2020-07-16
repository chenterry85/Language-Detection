from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import domain
import os

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        domain.init_freq_table()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.data_from_file = True
        self.selected_filename = StringVar()
        self.selected_filename.set("sample-text.txt")
        self.selected_filepath = "sample-text.txt"
        self.TEXT_BOX_WIDTH = 50
        self.TEXT_BOX_HEIGHT = 10

        current_row = 0

        self.space = Label(self, text=" ")
        self.space.grid(row = current_row,column = 0)

        current_row += 1

        self.l1 = Label(self, text="  Data Source:       ", pady=2)
        self.l1.grid(row = current_row, column = 0)

        self.chooser = StringVar()
        self.r1 = Radiobutton(self,
                            text="File",
                            variable=self.chooser,
                            value="1",
                            selectcolor="#F40088",
                            command= self.update_input_source)
        self.r1.grid(row = current_row, column=1, sticky=W)


        self.b1 = Button(self,text="Choose File", padx = 10, command = self.select_file_from_directory)
        self.b1.grid(row = current_row,column =2, sticky = W)

        self.l2 = Label(self,textvariable=self.selected_filename)
        self.l2.grid(row = current_row,column =2, columnspan = 1, sticky = E)

        current_row += 1

        self.r2 = Radiobutton(self,
                            text="Textbox",
                            variable=self.chooser,
                            value="2",
                            command= self.update_input_source)
        self.r2.grid(row = current_row, column=1, sticky=W)
        self.chooser.set("1")

        current_row += 1

        self.l3 = Label(self,text="  Text:")
        self.l3.grid(row=current_row, column=0,sticky = W)

        self.input = Text(self, width = self.TEXT_BOX_WIDTH, height = self.TEXT_BOX_HEIGHT, wrap = WORD,
                                bd = 6, bg = "#383838", fg = "#fff", insertbackground = "#FDFD96", insertwidth = 3  , spacing1 = 2)
        self.input.grid(row=current_row,column = 1, columnspan=2, sticky = W)

        current_row += 1

        self.b2 = Button(self,text="Scan", padx = 10, command = self.scan_text_from_data_source)
        self.b2.grid(row = current_row,column =2, columnspan = 1)

        self.b3 = Button(self,text="Clear", padx = 10, command = self.clear_textfield)
        self.b3.grid(row = current_row, column = 2,columnspan = 1, sticky=E)

        current_row += 1

        self.space2 = Label(self, text="")
        self.space2.grid(row = current_row,column = 2)

        current_row += 1

        self.l4 = Label(self, text = "  Language:")
        self.l4.grid(row = current_row,column = 0, columnspan = 1, sticky = W)

        self.output = Text(self, width = self.TEXT_BOX_WIDTH, height = 5, wrap = WORD, bd = 6)
        self.output.grid(row=current_row,column = 1, columnspan=2, sticky = W)
        self.set_text(self.output,"No input")

    def scan_text_from_data_source(self):

        if self.data_from_file:
            # data source as local file

            content = self.extract_local_file_data()
            self.set_text(self.output,domain.get_language(content))
        else:
            #data source as textbox
            content = self.input.get(1.0,END)
            if not content.rstrip():
                self.set_text("No input")
            else:
                self.set_text(domain.get_language(content))

    def select_file_from_directory(self):
        file_types = [('Text files', '*.txt *.rtf')]
        filepath = askopenfilename(filetypes = file_types)

        if os.path.getsize(filepath) <= 220:
            #empty file
            messagebox.showwarning(title="Warning", message="Selected file is empty!")
        else:
            #valid file
            self.selected_filepath = filepath
            self.selected_filename.set(self.extract_filename_from_filepath(filepath))


    def extract_local_file_data(self):
        filepath = self.selected_filepath
        with open(filepath, 'rt') as f:
            return f.read()

    def extract_filename_from_filepath(self, path):
        start_index = path.rindex("/") + 1
        filename = path[start_index:]
        return filename

    def update_input_source(self):
        self.data_from_file = True if self.chooser.get() == "1" else False

    def set_text(self,label,text):
        self.output.delete(1.0,END)
        label.insert(END,text)

    def clear_textfield(self):
        self.input.delete(1.0,END)
