from tkinter import*
import mysql.connector
from tkinter import messagebox

def firupdatefun():
    def updatef():
        inid = ide.get()
        inname = namee.get()
        ingender = gendere.get()
        inage = agee.get()
        inaddress = addresse.get()
        inmno = mnolbe.get()
        intitle = titlee.get()
        incmp = cmpe.get()
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="policedb")
        if (con):
            cur = con.cursor(prepared=True);

            pre_qry = "update fir set id=%s,name=%s,gender=%s,age=%s,address=%s,mno=%s,title=%s,complaint=%s where name=%s"
            cur.execute(pre_qry, (inid, inname, ingender, inage, inaddress, inmno, intitle, incmp,inname))
            con.commit();
            if cur.rowcount!=0:
                messagebox.showinfo("Update info", "Row updated successfully")

    def clearall():
        ide.delete(0,END)
        namee.delete(0,END)
        gendere.delete(0,END)
        agee.delete(0,END)
        addresse.delete(0, END)
        mnolbe.delete(0,END)
        titlee.delete(0, END)
        cmpe.delete(0,END)

    def search():

        check = False
        inid =ide.get()
        if inid =="":
            inid="0"
        inname=namee.get()
        con = mysql.connector.connect(host="localhost",
                                      user="root",
                                      passwd="",
                                      database="policedb")
        if (con):
            print("connection done")
            cur = con.cursor();
            qry = "select *from fir"
            cur.execute(qry)

            Mrows = cur.fetchall()
            con.commit()

            for row in Mrows:
                print("name:", row[0], "gender:", row[1],"and id=",inid)

                if int(inid) ==row[0] or inname==row[1]:
                    check = True
                    ide.delete(0,END);
                    ide.insert(0,row[0]);
                    namee.delete(0,END)
                    namee.insert(0,row[1])

                    gendere.insert(0,row[2])
                    agee.insert(0,row[3])
                    addresse.insert(0,row[4])
                    mnolbe.insert(0,row[5])
                    titlee.insert(0,row[6])
                    cmpe.insert(0,row[7])
                    con.close()
                    break
            # print(cur.rowcount, "Student Data Selected")
            if (check == False):
                messagebox.showinfo("ErrorMsg", "Invalid FIR ID")

            cur.close()
            con.close()
        else:
            print("Connection failed")

    searchwin=Tk()

    searchwin.iconbitmap("123.ico")
    searchwin.configure(background="light blue");

    searchwin.title("Search FIR");

    searchwin.geometry("600x400+400+200");

    idlbl = Label(searchwin, text="Enter id:",font="elephant 12");
    namelbl = Label(searchwin, text="Enter name:",font="elephant 12")
    genderlbl = Label(searchwin, text="Enter gender:",font="elephant 12")
    agelbl = Label(searchwin, text="Enter age:",font="elephant 12");

    addresslbl = Label(searchwin, text="Enter address:",font="elephant 12")
    mnolbl = Label(searchwin, text="Enter mobile no:",font="elephant 12")

    titlelbl = Label(searchwin, text="Enter title:",font="elephant 12")
    cmplbl = Label(searchwin, text="Enter complaint:",font="elephant 12")

    ide = Entry(searchwin,font="elephant 12");
    namee = Entry(searchwin,font="elephant 12");
    gendere = Entry(searchwin,font="elephant 12");
    agee = Entry(searchwin,font="elephant 12");

    addresse = Entry(searchwin,font="elephant 12");
    mnolbe = Entry(searchwin,font="elephant 12");

    titlee = Entry(searchwin,font="elephant 12");
    cmpe = Entry(searchwin,font="elephant 12");

    idlbl.grid(row=0, column=1)
    ide.grid(row=0, column=2)
    namelbl.grid(row=1, column=1)
    namee.grid(row=1, column=2)
    genderlbl.grid(row=2, column=1)
    gendere.grid(row=2, column=2)
    agelbl.grid(row=3, column=1)
    agee.grid(row=3, column=2)
    addresslbl.grid(row=4, column=1)
    addresse.grid(row=4, column=2)
    mnolbl.grid(row=5, column=1)
    mnolbe.grid(row=5, column=2)
    titlelbl.grid(row=6, column=1)
    titlee.grid(row=6, column=2)
    cmplbl.grid(row=7, column=1)
    cmpe.grid(row=7, column=2)

    btn=Button(searchwin,text="SearchFIR",command=search)
    btn.grid(row=20,column=30)
    btnclear=Button(searchwin,text="Clear",command=clearall)
    btnclear.grid(row=20,column=33)

    btnupdate=Button(searchwin,text="update",command=updatef)
    btnupdate.grid(row=20,column=35)
