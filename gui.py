#!/usr/bin/python3

from tkinter import *
from tkinter import ttk


class Program:


    def __init__(self,master):
        master.option_add('*tearoff',False)
        master.title('Point System')
        self.menubar=Menu(master)
        master.config(menu = self.menubar)
        self.file=Menu(self.menubar)
        
        self.menubar.add_cascade(menu=self.file, label='File')
        
        self.frame_header= ttk.Frame(master)
        self.frame_header.pack()
        ttk.Label(self.frame_header, text = 'Coming Soon', style = 'Header.TLabel').grid(row = 0, column = 1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()




def main():
    root = Tk()
    program = Program(root)
    root.mainloop()
    
if __name__ == "__main__": main()
