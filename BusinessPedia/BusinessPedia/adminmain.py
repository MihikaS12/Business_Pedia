from tkinter import *
from tkinter import*
from bizinsert import*
from deletebiz import*
from updatebiz import*
from serachbiz import*
from bizinsert import*
from register import*
from adminmain import*
from usermain import*
import mysql.connector
from tkinter import messagebox
from PIL import ImageTk,Image
def insertfun():
    pass

def adminhelp():
    pass
def copyright():
    pass
def changepass():
    print("change pass called")
def admincont():
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    root = Tk()
    root.iconbitmap("123.ico")
    root.configure(background="red");

    root.geometry("500x500+400+200");
    root.title("Admin Control Window")

    imglbl=Label(root,text="WELCOME",font="forte 20",width=100);


    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Change Password", command=changepass)
    filemenu.add_command(label="Register User", command=insfunreg)

    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Admin", menu=filemenu)

    msmenu = Menu(menubar, tearoff=0)
    msmenu.add_command(label="insert", command=donothing)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Add New", command=bizinsertfun)

    editmenu.add_command(label="Search", command=titlesearch)

    editmenu.add_separator()

    editmenu.add_command(label="Update", command=firupdatefun)
    editmenu.add_command(label="Delete", command=firdeletefun)

    menubar.add_cascade(label="Business", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About Project", command=donothing)
    helpmenu.add_command(label="CopyRight", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    imglbl.place(anchor=S)
    imglbl.pack()
    root.mainloop()
