from Tkinter import *

PAD = 50

class Application(Frame):

    def createWidgets(self):
        pass

    def get_padding(self):
        return PAD

    def __init__(self):
        self.root = Tk()
        self.PAD = 10
        Frame.__init__(self, self.root)
        self.pack()
        self.createWidgets()
        self.mainloop()

    def close(self):
        self.root.destroy()