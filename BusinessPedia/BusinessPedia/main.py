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
def start():

    def login():

        def logincheck1():
            #fetch user and password from  tkinter form
            name=ename.get()
            passw=epass.get()

            check=False
            #fetch data from mysql table

            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="",
                                          database="businessdb")
            if (con):
                print("connection done")
                cur = con.cursor();
                qry = "select *from users where usertype='user'"
                cur.execute(qry)

                Mrows = cur.fetchall()
                con.commit()

                for row in Mrows:
                    print("Username:",row[1],"Userpass:",row[2])

                    if name == row[1] and passw==row[2] :
                            check=True
                            mw.wm_withdraw()
                            usercont()
                            con.close()
                            break
                   # print(cur.rowcount, "Student Data Selected")
                if(check==False):
                    messagebox.showinfo("ErrorMsg", "Invalid username or password")

                cur.close()
                con.close()
            else:
                print("Connection failed")

            #-----------------------

        def logincheck2():
            #fetch user and password from  tkinter form
            name=ename.get()
            passw=epass.get()

            check=False
            #fetch data from mysql table

            con = mysql.connector.connect(host="localhost",
                                          user="root",
                                          passwd="",
                                          database="businessdb")
            if (con):
                print("connection done")
                cur = con.cursor();
                qry = "select *from users where usertype='admin'"
                cur.execute(qry)

                Mrows = cur.fetchall()
                con.commit()

                for row in Mrows:
                    print("Username:",row[1],"Userpass:",row[2])

                    if name == row[1] and passw==row[2] :
                            check=True
                            mw.wm_withdraw()
                            admincont()
                            con.close()
                            break
                   # print(cur.rowcount, "Student Data Selected")
                if(check==False):
                    messagebox.showinfo("ErrorMsg", "Invalid username or password")

                cur.close()
                con.close()
            else:
                print("Connection failed")

        mw=Tk()
        mw.iconbitmap("123.ico")
        mw.geometry("600x400+400+200")
        mw.title("Business Pedia Login")
        mw.configure(background="grey");

        lbl1=Label(mw,text="User Name",font="Elephant 15",width=10);
        lbl2=Label(mw,text="User Pasword",font="Elephant 15",width=10);
        ename=Entry(mw,font="Elephant 15",width=15)
        epass=Entry(mw,show="*",font="Elephant 15",width=15)
        loginbtn1=Button(mw,text="User login",command=logincheck1,font="Elephant 10",width=20)
        loginbtn2= Button(mw, text="Admin login", command=logincheck2,font="Elephant 10",width=20)

        regbtn=Button(mw,text="Register",command=insfunreg,font="Elephant 10",width=20)
        lbl1.grid(row=1,column=1,padx=20,pady=40)
        ename.grid(row=1,column=2,padx=40,pady=40)
        lbl2.grid(row=2, column=1,padx=39,pady=40)
        epass.grid(row=2, column=2,padx=40,pady=40)
        loginbtn1.grid(row=3,column=1,padx=40,pady=2)
        loginbtn2.grid(row=4, column=1,padx=40,pady=2)

        regbtn.grid(row=5,column=1,padx=40,pady=2)
        mw.mainloop()

    login()
