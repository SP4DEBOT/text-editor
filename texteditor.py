import sys

#main window

from tkinter import *
from tkinter import filedialog



root  = Tk() #creates the main application 
root.title("Text-Editor")

main_frame = Frame(root)
main_frame.pack(pady=5)



def new_file():
    text.delete("1.0",END) #deletes already existed text


def open_file():
    text.delete("1.0",END)

    #Filename 
    text_file = filedialog.askopenfilename(
        initialdir="/", 
        title="open your file",
        filetypes=[("Text files","*.txt"),("Html files","*.html"),("All files","*.*")])
    
    text_file = open(text_file,'r')
    #Read contents
    read_file = text_file.read()
    #Clear the widget
    text.delete("1.0",END)
    text.insert(END,read_file)
    text_file.close()

def save_file():
    save_text = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save your file",
        filetypes=[
            ("All files","*.*")
        ]
    )
    text.get("1.0",END)
    #create file
    save_fi = open(save_text,"w+")
    save_fi.write()
    save_fi.close()

    

def quiit():
    root.quit()

#scrollbar
scrollbar = Scrollbar(main_frame)
scrollbar.pack(side=RIGHT,fill=Y)

text = Text(main_frame,selectbackground="blue") #creates text object
text.pack()

#Menu Bar
menu_bar = Menu(root,title="Menu")
root.config(menu=menu_bar)

#Sub menu
sub_menu = Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(label="File", menu=sub_menu)

# Sub menu operations
sub_menu.add_command(label="New", command=new_file)
sub_menu.add_command(label="Open", command=open_file)
sub_menu.add_command(label="Save" , command=save_file)
sub_menu.add_command(label="Save As")
sub_menu.add_separator()
sub_menu.add_command(label="Exit" ,command=quiit)

#Edit menu

edit_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Delete")






scrollbar.config(command=text.yview)
text.config(yscrollcommand = scrollbar.set)



root.mainloop() 


