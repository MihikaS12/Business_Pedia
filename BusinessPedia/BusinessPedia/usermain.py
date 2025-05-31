from tkinter import *
from bizinsert import*
from serachbiz import*
from deletebiz import*
from updatebiz import*
from register import*


def usercont():
    def donothing():
        filewin = Toplevel(root)
        button = Button(filewin, text="Do nothing button")
        button.pack()


    root = Tk()

    root.iconbitmap("123.ico")
    root.configure(background="red");

    imglbl=Label(root,text="WELCOME",font="forte 20",width=100);


    root.geometry("500x400+200+100");
    root.title("user Control Window");

    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Change Password", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="User", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Search Business", command=titlesearch)

    editmenu.add_separator()

    editmenu.add_command(label="Search Person", command=personsearch)
    editmenu.add_command(label="Search Company", command=companysearch)

    menubar.add_cascade(label="Search", menu=editmenu)

    root.config(menu=menubar)
    imglbl.pack()
    root.mainloop()
