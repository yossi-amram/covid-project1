from tkinter import *
from tkinter import ttk


class Covid19App:

    def __init__(self,master):
        
        location=StringVar()
        self.combobox=ttk.Combobox(master,textvariable=location)
        self.combobox.config(values=['Algeria','Israel'])
        



def main():
    root = Tk()
    app = Covid19App(root)



if __name__=="__main__" :
    main()
    