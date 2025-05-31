# Import Module
from tkinter import *
import time
from main import*
from threading import *

# Create Object
root = Tk()

# Set geometry
root.geometry("1366x768")
root.iconbitmap("123.ico")
root.configure(background="orange");
root.title("POLICE FIR SYSTEM")
lb1=Label(root,text="WELCOME TO POLICE FIR SYSTEM",bg="red",fg="white",font=("broadway",40))

lb2=Label(root,text="F",bg="black",fg="white",font=("broadway",35))
lb3=Label(root,text="I",bg="black",fg="white",font=("broadway",35))
lb4=Label(root,text="R",bg="black",fg="white",font=("broadway",35))
lb5=Label(root,text="System",bg="red",fg="black",font=("broadway",35))

# use threading

def threading():
	# Call work function
	t1=Thread(target=work)
	t1.start()

# work function
def work():
    time.sleep(1)
    lb1.place(x=200,y=40)
    time.sleep(1)
    lb2.place(x=420,y=280)
    time.sleep(1)
    lb3.place(x=520,y=280)

    time.sleep(1)
    lb4.place(x=620,y=280)
    time.sleep(1)
    lb5.place(x=720,y=280)
    time.sleep(5)
    root.clipboard_clear()
    start()

# Create Button
threading()
# Execute Tkinter


root.mainloop()

