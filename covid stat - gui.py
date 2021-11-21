
from tkinter import *
from tkinter import ttk
import numpy

#importing my data library
import covid_data


#creats a combobox and set (could help avoid a bit of code repetition)
def create_combobox(master,variable,choice_tup):
    tempCombo=ttk.Combobox(master,textvariable=variable)
    tempCombo.config(values=choice_tup)
    return tempCombo


class Covid19App:

    def __init__(self, master, filename):
        
        #get the locations
        self.data = covid_data.covidData(filename)
        df=self.data.globalDF
        locations = numpy.unique(df['location'].values)



        #gui

        #1 - death graph
        #combobox
        self.location=StringVar()
        self.combobox1=create_combobox(master,self.location,tuple(locations))
        self.combobox1.grid(column=0,row=0)

        #checkbox
        self.iaAbsolute=BooleanVar()
        self.checkbox=ttk.Checkbutton(master=master,text="per million ppl",onvalue=False,offvalue=True,variable=self.iaAbsolute)
        self.checkbox.grid(row=1,column=0)
        
        #button
        ttk.Button(master,text="Create Death Graph",command=self.death_graph).grid(column=0,row=2,columnspan=2)

        #spacer
        ttk.Label(master,text=" ").grid(column=0,row=3,columnspan=2,rowspan=1)

        #label
        self.file_label=ttk.Label(master,text="")
        self.file_label.grid(column=0,row=4,columnspan=2,rowspan=1)

        #spacer
        ttk.Label(master,text="\n\n ").grid(column=0,row=5,columnspan=2,rowspan=1)


        #2 - Histogram
        #button
        ttk.Button(master,text="Create Death Histogram",command=self.death_histo_abs).grid(column=0,row=6,columnspan=2)

        #label
        self.file_label2=ttk.Label(master,text="")
        self.file_label2.grid(column=0,row=7,columnspan=2,rowspan=1)

        #spacer
        ttk.Label(master,text="\n ").grid(column=0,row=8,columnspan=2,rowspan=1)

        #button
        ttk.Button(master,text="Create Death Histogram\nPer Million",command=self.death_histo_per).grid(column=0,row=9,columnspan=2)

        #label
        self.file_label3=ttk.Label(master,text="")
        self.file_label3.grid(column=0,row=10,columnspan=2,rowspan=1)

        

    #creates the image of the graph
    def death_graph(self):
        file_str=self.data.create_graph(self.location.get(),absolute=self.iaAbsolute.get())
        self.file_label.config(text="look in folder for:\n"+file_str)




    #creates the image of the histogram in absolute numbers
    def death_histo_abs(self):
        file_str=self.data.create_histogram(self.data.today,True)
        self.file_label2.config(text="look in folder for:\n"+file_str)

    #creates the image of the histogram for deaths per million
    def death_histo_per(self):
        file_str=self.data.create_histogram(self.data.today,False)
        self.file_label3.config(text="look in folder for:\n"+file_str)



def main():
    root = Tk()
    app = Covid19App(root, 'owid-covid-data.xlsx')
    root.mainloop()


if __name__=="__main__" :
    main()
    