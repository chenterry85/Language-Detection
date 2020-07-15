from tkinter import *
from PIL import ImageTk, Image

let = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lang_freq = {}
text_freq = []
data = []

def getInputText():
    with open('text.txt') as f:
        return f.read()

def getData():
    input = []
    with open('data.csv') as f:
        for line in f:
            input.append(line.rstrip().split(","))
    return input

def letter_size(text):
    sum = 0
    for i in let:
        sum += text.count(i)
    return sum

def getPercentSimilar(lang):
    diff = 0
    for i in range(1,len(data) - 1):
        diff += abs(text_freq[i] - lang_freq[lang][i])
    return "{}%".format(round(100 - diff,2))

def getLanguage(text):
    text_freq[:] = []
    print(data[0])
    for c in range(1,len(data[0])):
        l = []
        for r in range(1,len(data)):
            if data[r][c][-1] == '%':
                l.append(float(data[r][c][:-1]))
            else:
                l.append(float(data[r][c]))
        lang_freq[data[0][c]] = l

    #generate text's letter frequency
    TEXT_LENGTH = letter_size(text)
    for i in let:
        text_freq.append(text.count(i)/(TEXT_LENGTH * 1.0) * 100)

    #compare each lang's freq to the text's freq
    min_dif = [10000000,10000000,10000000,10000000,10000000]
    min_dif_lang = ["","","","",""]
    for c in range(1,len(data[0])):
        sum = 0
        for r in range(1,len(data) - 1):
            sum += abs(text_freq[r] - lang_freq[data[0][c]][r])
        for i in range(len(min_dif)):
            if sum < min_dif[i]:
                if i + 4 < len(min_dif):
                    min_dif[i + 4] = min_dif[i + 3]
                    min_dif_lang[i + 4] = min_dif_lang[i + 3]
                if i + 3 < len(min_dif):
                    min_dif[i + 3] = min_dif[i + 2]
                    min_dif_lang[i + 3] = min_dif_lang[i + 2]
                if i + 2 < len(min_dif):
                    min_dif[i + 2] = min_dif[i + 1]
                    min_dif_lang[i + 2] = min_dif_lang[i + 1]
                if i + 1 < len(min_dif):
                    min_dif[i + 1] = min_dif[i]
                    min_dif_lang[i + 1] = min_dif_lang[i]
                min_dif[i] = sum
                min_dif_lang[i] = data[0][c]
                break

    result = ""
    for i in range(len(min_dif_lang)):
        result += "{}. {} - Similarity: {}\n".format(i + 1,min_dif_lang[i],getPercentSimilar(min_dif_lang[i]))
    return result

class Application(Frame):

    def __init__(self,master):
        global data
        Frame.__init__(self,master)
        data = getData()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.get_data_from_file = True
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

        # self.output_text = StringVar()
        # self.output_text.set("No output")
        # self.result = Label(self, textvariable = self.output_text)
        # self.result.grid(row = 4, column = 1, sticky = W)

        self.output = Text(self, width = self.TEXT_BOX_WIDTH, height = 5, wrap = WORD)
        self.output.grid(row=4,column = 1, columnspan=2, sticky = W)
        self.setText("No input")

    def buttonAction(self):
        content = ""
        if self.get_data_from_file:
            content = getInputText()
            self.setText(getLanguage(content))
        else:
            content = self.input.get(1.0,END)
            if not content.rstrip():
                self.setText("No input")
            else:
                self.setText(getLanguage(content))

    def updateChoice(self):
        if self.chooser.get() == "1":
            self.get_data_from_file = True
        else:
            self.get_data_from_file = False

    def setText(self,text):
        self.output.delete(1.0,END)
        self.output.insert(END,text)

    def clear(self):
        self.input.delete(1.0,END)

#display
root = Tk()
root.minsize(width=540,height=330)
root.maxsize(width=540,height=330)
root.title("Guess Language Lab")
app = Application(root)
root.mainloop()
