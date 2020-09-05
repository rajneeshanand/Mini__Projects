from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

root = Tk()
root.geometry("634x400")
root.title("Untitled-Notepad")
root.wm_iconbitmap("np.png")
#TODO:Adding text area
TextArea = Text(root, font="lucida 12")
file =None
TextArea.pack(expand=True, fill = BOTH)

#TODO:Defining Function
def cut():
    TextArea.event_generate("<<Cut>>")
def copy():
    TextArea.event_generate("<<Copy>>")
def paste():
    TextArea.event_generate("<<Paste>>")
def about():
    tmsg.showinfo("Notepad","preapred by Rajneesh Anand If you've any issue mail to rajneesh.1491981@gmail.com")
def quitapp():
    root.destroy()
def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0, END)
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt",filetypes=[("All files", "*.*"), ("Text documents", "*.*")])
        if file=="":
            file=None
        else:
            f=open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def openfile():
    global file
    if file==None:
        file = askopenfilename(defaultextension=".txt",
                                 filetypes=[("All files", "*.*"), ("Text documents", "*.*")])
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file) + "-Notepad")
            TextArea.delete(1.0, END)
            f=open(file, "r")
            TextArea.insert(1.0, f.read())
            f.close()





#TODO:creating menu
MenuBar = Menu(root)
filemenu = Menu(MenuBar,tearoff =0)
filemenu.add_command(label ="New",command=newfile)
filemenu.add_command(label ="Open",command=openfile)
filemenu.add_command(label ="Save",command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quitapp)
MenuBar.add_cascade(label="file", menu=filemenu)
editmenu = Menu(MenuBar, tearoff=0)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)
MenuBar.add_cascade(label="Edit", menu=editmenu)
Helpmenu = Menu(MenuBar, tearoff=0)
Helpmenu.add_command(label="About", command=about)
MenuBar.add_cascade(label="Help", menu = Helpmenu)
root.config(menu=MenuBar)
scroll=Scrollbar(TextArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview())
TextArea.config(yscrollcommand=scroll.set)


root.mainloop()