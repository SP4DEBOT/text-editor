import sys

#main window

from tkinter import *
from tkinter import filedialog



root  = Tk() #creates the main application 

text = Text(root) #creates text object
text.grid(row=0,column=0)

def saveas():
    global text
    t = text.get("1.0","end-1c")
    save_loc  = filedialog.asksaveasfilename()
    file1 = open(save_loc,"w+")
    file1.write(t)
    file1.close()
    button = Button(root,text="save",command=saveas)
    button.grid(row=1,coloumn=0)

root.title("Text-Editor")
root.mainloop() 


