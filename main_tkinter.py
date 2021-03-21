import tkinter as tk
from tkinter import messagebox, Entry
from merge import solution
import random
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_execute()
        self.create_textbox()
        self.create_quit()

    def random(self):
        opL = []
        i = 0
        while i < 10:
            opL.append(random.randint(1, 10000))
            i += 1
        return opL

    def create_textbox(self):
        self.input = Entry(self.master)
        self.input.pack()   

    def create_execute(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Execute"
        self.hi_there["command"] = self.execute
        self.hi_there.pack(side="top")
        
    def data_retrival(self):              
        self.data = self.input.get()
        if len(self.data) >= 1:
            if "random" in (self.data).lower():
                return self.random()
            else:
                print((self.data).split())
                return (self.data).split()
        else:
            self.message_box("Please input a number sequence")

    def create_quit(self):
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def message_box(self, info):
        messagebox.showinfo(title="Results", message=info)

    def execute(self):
        self.solutions = solution(self.data_retrival())
        self.message_box(self.solutions)
        
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()