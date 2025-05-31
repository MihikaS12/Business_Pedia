# Import Module
from tkinter import *
import time
from main import*
from threading import *
from playsound import playsound

# Create Object
root = Tk()

# Set geometry
root.geometry("1366x768")
root.iconbitmap("2.ico")
root.configure(background="orange");
root.title("Business Pedia")
lb1=Label(root,text="WELCOME TO BUSINESS PEDIA",bg="red",fg="white",font=("elephant",40))

lb2=Label(root,text="BUSI",bg="black",fg="white",font=("elephant",35))
lb3=Label(root,text="NE",bg="black",fg="white",font=("elephant",35))
lb4=Label(root,text="SS",bg="black",fg="white",font=("elephant",35))

lb5=Label(root,text="Encyclopedia",bg="black",fg="white",font=("elephant",35))

# use threading

def threading():
	# Call work function
	t1=Thread(target=work)
	t1.start()

# work function
def work():
   # playsound('Alarm04.wav')
    time.sleep(1)
    lb1.place(x=170,y=40)

    time.sleep(.5)
    lb2.place(x=220,y=280)
    time.sleep(.5)

    lb3.place(x=380,y=280)

    time.sleep(.5)

    lb4.place(x=480,y=280)
    time.sleep(.5)

    lb5.place(x=580,y=280)

    time.sleep(3)
    start()

# Create Button
threading()
# Execute Tkinter


root.mainloop()

