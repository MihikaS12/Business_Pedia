from tkinter import*
import mysql.connector
from tkinter import messagebox

def insfunreg():
    def insert():
        inname =ename.get()
        inpass=epass.get()
        intype=etype.get()
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="businessdb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "insert into users values(%s,%s,%s)"
            cur.execute(pre_qry, (inname,inpass,intype))
            con.commit();

            messagebox.showinfo("Insert info", "Row inserted successfully")

    inswin=Tk()
    inswin.geometry("400x400+300+200");
    lbname = Label(inswin, text="Enter user name:");
    lbpass = Label(inswin, text="Enter user password:")
    lbtype = Label(inswin, text="Enter user type(admin/user):")

    ename=Entry(inswin);
    epass = Entry(inswin);
    etype=Entry(inswin);
    lbname.grid(row=0, column=0)
    ename.grid(row=0, column=20)
    lbpass.grid(row=10, column=0)
    epass.grid(row=10, column=20)
    lbtype.grid(row=20, column=0)
    etype.grid(row=20, column=20)

    btn=Button(inswin,text="insertData",command=insert)
    btn.grid(row=20,column=30)
