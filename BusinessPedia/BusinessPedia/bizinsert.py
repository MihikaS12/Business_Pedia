from tkinter import*
import mysql.connector
from tkinter import messagebox

def bizinsertfun():
    def insert():
        intitle =titlee.get()
        incom=come.get()
        inperson=persone.get()
        inweb=webe.get()
        indetail = detaile.get()
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="policedb")
        if (con):
            cur = con.cursor(prepared=True);
            pre_qry = "insert into bizpedia values(%s,%s,%s,%s,%s)"
            cur.execute(pre_qry, (intitle,incom,inperson,inweb,indetail))
            con.commit();

            messagebox.showinfo("Insert info", "Row inserted successfully")

    inswin=Tk()

    inswin.iconbitmap("123.ico")
    inswin.configure(background="light green");



    inswin.title("Add New Business");

    inswin.geometry("600x400+300+200");
    titlelbl = Label(inswin, text="Enter Title:",font="elephant 12");
    comlbl = Label(inswin, text="Enter Compnany name:",font="elephant 12")
    personlbl = Label(inswin, text="Enter Person:",font="elephant 12")
    weblbl = Label(inswin, text="Enter website:",font="elephant 12");

    detaillbl = Label(inswin, text="Enter Business Detail:",font="elephant 12")

    titlee = Entry(inswin,font="elephant 12");
    come = Entry(inswin,font="elephant 12");
    persone = Entry(inswin,font="elephant 12");
    webe = Entry(inswin,font="elephant 12");

    detaile = Entry(inswin,font="elephant 12");
    titlelbl.grid(row=0, column=1)
    titlee.grid(row=0, column=2)
    comlbl.grid(row=1, column=1)
    come.grid(row=1, column=2)
    personlbl.grid(row=2, column=1)
    persone.grid(row=2, column=2)
    detaillbl.grid(row=3, column=1)
    detaile.grid(row=3, column=2)

    btn=Button(inswin,text="insertData",command=insert)
    btn.grid(row=20,column=30)
