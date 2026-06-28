import sys

#main window

from tkinter import *
from tkinter import filedialog



root  = Tk() #creates the main application 
root.title("Text-Editor")

main_frame = Frame(root)
main_frame.pack(pady=5)

#scrollbar
scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT,fill=Y)

text = Text(main_frame,selectbackground="yellow") #creates text object
text.pack()



scrollbar.config(command=text.yview)
text.config(yscrollcommand = scrollbar.set)



root.mainloop() 


