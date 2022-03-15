from tkinter import *
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector as sql

#Setting up main window
root=Tk()
root.geometry('900x650+250+20')
root.title('C H E R R I')


#-------------------------------------------------MySql Back-end-----------------------------------------------------------------
#This will check weather user have database if not database will be created!
#And then it will create table 'register'

con = sql.connect(host='localhost',user='root',passwd='root')
cur = con.cursor(buffered=True)
cur.execute('show databases;')
data = cur.fetchall()
is_made = False
for data in data:   #if database exist
        if data == ("cherri",):
            cur.execute("use cherri")
            is_made = True
if not is_made: #if don't exist make new one
        cur.execute("create database cherri;")
        cur.execute("use cherri")
        cur.execute("create table Register(id int auto_increment primary key,f_name varchar(20),l_name varchar(20),\
            contact bigint(10),email varchar(50),question varchar(100),answer varchar(100),password varchar(50))")
        con.commit()

#-------------------------------------------------Fuctions Front-end-------------------------------------------------------------
def main_window():
    cherri = Image.open('Images/Interface1.png')
    image = cherri.resize((900,650), Image.ANTIALIAS)
    logo=ImageTk.PhotoImage(image)
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1,row=0)

    def bttn1(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(root,width=25,height=3,command=lambda:show_login(),text=text,fg=bcolor,\
            bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,)
        my_button1.place(x=210,y=450)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)

    def bttn2(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(root,width=25,height=3,command=lambda:show_sigin(),text=text,\
            fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,)
        my_button1.place(x=500,y=450)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)
    
    bttn1(0,0,"Login",'#ffcc66',"#141414")
    bttn2(0,0,"Sign up",'#EB46CD',"#141414")

def show_sigin():
    cherri = Image.open('Images/RegisterFrame.png')
    image = cherri.resize((900,650), Image.ANTIALIAS)
    logo=ImageTk.PhotoImage(image)
    logo_label =Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1,row=0)
    
    def back_bttn(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(root,width=25,height=3,command=lambda:main_window(),text=text,\
            fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,)
        my_button1.place(x=60,y=550)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)
    
    back_bttn(0,0,"Home",'#ffcc66',"#141414")
    
    frame1 = Frame(root,width=585,height=620,bg='#7D46EB')                  #purple color                                                 
    frame1.place(x=300,y=13)
    title_frame = Label(frame1,text='Sign Up',font=("Arial Bold",35),bg='#7D46EB')
    title_frame.place(x=180,y=0)
    N_frame = Label(frame1,text="It's quick and easy.",font=("Arial",20),bg='#7D46EB')
    N_frame.place(x=160,y=58)
    firstName_main=Label(frame1,text='First name',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    firstName_main.place(x=50,y=140)
    firstName = Entry(frame1,bg='#ADA3BF',font=("Arial",12,'bold'))
    firstName.place(x=50,y=175,width=175,heigh=30)

    lastName_main=Label(frame1,text='Last name',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    lastName_main.place(x=300,y=140)
    lastName = Entry(frame1,bg='#ADA3BF',font=("Arial",12,'bold'))
    lastName.place(x=300,y=175,width=175,heigh=30)

    Cntnum_main=Label(frame1,text='Contact number',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    Cntnum_main.place(x=50,y=240)
    Cntnum = Entry(frame1,bg='#ADA3BF',font=("Arial",12,'bold'))
    Cntnum.place(x=50,y=275,width=175,heigh=30)

    email_main=Label(frame1,text='Email',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    email_main.place(x=300,y=240)
    email = Entry(frame1,bg='#ADA3BF',font=("Arial",12,'bold'))
    email.place(x=300,y=275,width=175,heigh=30)

    srt_main=Label(frame1,text='Security question',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    srt_main.place(x=50,y=340)
    comboque=Combobox(frame1,font=('times new roman',12),state='readonly')
    comboque['values']=('Select','Your first pet name?','Your birth place?',\
        'Your best friend name?','Your favourite teacher?','Your hobbie?')
    comboque.current(0)
    comboque.place(x=50,y=375,width=175,height=30)
  

    ans_main=Label(frame1,text='Answer',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    ans_main.place(x=300,y=340)
    ans= Entry(frame1,bg='#ADA3BF',font=("Arial",12,'bold'))
    ans.place(x=300,y=375,width=175,heigh=30)

    passwd_main=Label(frame1,text='Password',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    passwd_main.place(x=50,y=440)
    passwd = Entry(frame1,bg='#ADA3BF',font=("Arial",15,'bold'),show='*')
    passwd.place(x=50,y=475,width=175,heigh=30)
    
    confirm_main=Label(frame1,text='Confirm password',font=("Arial",15,'bold'),bg='#7D46EB',fg='#FFFFFF')
    confirm_main.place(x=300,y=440)
    confirm = Entry(frame1,bg='#ADA3BF',font=("Arial",15,'bold'),show='*')
    confirm.place(x=300,y=475,width=175,heigh=30)

    def clear():                   #This fuction fill clear all the text after succesfull register
        firstName.delete(0,END)
        lastName.delete(0,END)
        Cntnum.delete(0,END)
        email.delete(0,END)
        ans.delete(0,END)
        passwd.delete(0,END)
        confirm.delete(0,END)
        comboque.current(0)
       
    def register_now():
        if firstName.get()=='' or lastName.get()=='' or Cntnum.get()=='' or\
             email.get()=='' or ans.get()=='' or passwd.get()=='' \
            or confirm.get()=='' or comboque.get()=='Select':
            messagebox.showerror('Error','All Fields Are Required')
        elif passwd.get()!=confirm.get():
            messagebox.showerror('Error','Password Mismatch')
        else:
            try:
                cur.execute("use cherri")
                query=f"select *from register where email=%s"
                values = (email.get(),)
                cur.execute(query,values)
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error',"User already exists")
                else:
                    query = f"insert into register (f_name, l_name, email, contact,\
                         question, answer, password) values('{firstName.get()}','{lastName.get()}',\
                             '{email.get()}',{Cntnum.get()}, '{comboque.get()}','{ans.get()}',\
                                 '{passwd.get()}')"
                    cur.execute(query)
                    con.commit()
                    messagebox.showinfo('Success','Registration Succesfull')
                    clear()
                    main_window()
            except Exception as e:
                messagebox.showerror('Error',f'Error is due to\n{e}')
            
           
    def register_bttn(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(frame1,width=25,height=3,command=lambda:register_now(),text=text,\
            fg=bcolor,bg=fcolor,border=0,\
            activeforeground=fcolor,activebackground=bcolor,)
        my_button1.place(x=190,y=570)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)
    register_bttn(0,0,"Register Now",'#26ABED',"#141414")

def show_login():
    cherri1 = Image.open('Images/Email.png')
    image = cherri1.resize((900,650), Image.ANTIALIAS)
    logo=ImageTk.PhotoImage(image)
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1,row=0)
    def back_bttn(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(root,width=25,height=3,command=lambda:main_window(),\
            text=text,fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,)
        my_button1.place(x=10,y=590)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)
    
    back_bttn(0,0,"Home",'#30EB3C',"#141414")

    email = Entry(root,bg='white',font=("Arial",15,'bold'), borderwidth=0)
    email.place(x=330,y=202,width=250,heigh=35)

    passwd = Entry(root,bg='white',font=("Arial",15,'bold'),show='*', borderwidth=0)
    passwd.place(x=330,y=312,width=250,heigh=35)

    def Login_bttn():
        querry='select *from register where email=%s and password=%s'
        values=(email.get(),passwd.get())
        cur.execute(querry,values)
        data=cur.fetchone()
        if data==None:
            messagebox.showerror('Error',"Invalid Email or Password")


    def reset_pass():
        #This will create a Toplevel window on root
        
        root2 = Toplevel()
        root2.title('Forgot Password')
        root2.geometry('550x600+432+40')
        root2.focus_force()
        root2.grab_set()

        img = ImageTk.PhotoImage(Image.open("Images/Forgot.png"))
        label = Label(root2, image=img)
        label.pack()
        
        global Email 
        Email = Entry(root2,bg='#c9e265',font=("Arial",15,'bold'), borderwidth=0,cursor='hand2')
        Email.place(x=180,y=222,width=210,heigh=35)

        Comboque=Combobox(root2,font=('times new roman',12),state='readonly')
        Comboque['values']=('Select','Your first pet name?','Your birth place?',\
            'Your best friend name?','Your favourite teacher?','Your hobbie?')
        Comboque.current(0)
        Comboque.place(x=200,y=375,width=175,height=30)

        Ans = Entry(root2,bg='#c9e265',font=("Arial",15,'bold'), borderwidth=0,cursor='hand2')
        Ans.place(x=180,y=480,width=210,heigh=35)

        def change_pass():
            if Email.get()=='' or Comboque=='Select' or Ans.get()=='':
                messagebox.showerror('Error','All Field Required',parent=root2)
            else:
                cur.execute('use cherri')
                querry='select *from register where email=%s and question=%s and answer=%s'
                values = (Email.get(),Comboque.get(),Ans.get())
                cur.execute(querry,values)
                data=cur.fetchone()
                if data==None:
                    messagebox.showerror('Error',"Incorrect Field")
                else: 
                    frame3 = Frame(root2,width=585,height=620,bg='black')
                    frame3.pack()
                    frame3.place(x=0,y=0)
                    cherri = Image.open('Images/Confirm.png')
                    image = cherri.resize((550,600), Image.ANTIALIAS)
                    logo=ImageTk.PhotoImage(image)
                    logo_label = Label(frame3,image=logo)
                    logo_label.image = logo
                    logo_label.grid(column=1,row=0)
                    logo_label.pack()

                    new_pass = Entry(root2,bg='#e6e1dd',font=("Arial",15,'bold'), borderwidth=0,cursor='hand2')
                    new_pass.place(x=160,y=175,width=250,heigh=30)

                    con_pass = Entry(root2,bg='#e6e1dd',font=("Arial",15,'bold'), borderwidth=0,cursor='hand2')
                    con_pass.place(x=160,y=380,width=250,heigh=30)

                    def update_pass():
                        querry='UPDATE register SET password =%s WHERE email=%s;'
                        values = (new_pass.get(),Email.get())
                        cur.execute(querry,values)
                        con.commit()                   
                        messagebox.showinfo('Success','Password reset Succesfully',parent=root2)
                        root2.destroy()
                        show_login()

                    def confirm_pass(x,y,text,bcolor,fcolor):
                        def on_enter(e):
                            my_button1['background']=bcolor
                            my_button1['foreground']=fcolor
                        def on_leave(e):
                            my_button1['background']=fcolor
                            my_button1['foreground']=bcolor
                        my_button1 = Button(root2,width=25,height=3,command=lambda:update_pass(),\
                            text=text,fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,)
                        
                        my_button1.place(x=190,y=500)
                        my_button1.bind('<Enter>',on_enter)
                        my_button1.bind('<Leave>',on_leave)
                    
                    confirm_pass(0,0,"Confirm",'#30EB3C',"#141414")
                          
        def OK_bttn(x,y,text,bcolor,fcolor):
            def on_enter(e):
                my_button1['background']=bcolor
                my_button1['foreground']=fcolor
            def on_leave(e):
                my_button1['background']=fcolor
                my_button1['foreground']=bcolor
            my_button1 = Button(root2,width=25,height=3,\
                text=text,fg=bcolor,bg=fcolor,border=0,command=lambda:change_pass(),activeforeground=fcolor,activebackground=bcolor,)
            my_button1.place(x=248,y=540,width=80,height=40)
            my_button1.bind('<Enter>',on_enter)
            my_button1.bind('<Leave>',on_leave)
    
        OK_bttn(0,0,"OK",'#65e2bc',"#141414")

        root2.resizable(False, False)
        root2.mainloop()
     
    def login_bttn_ok():
        if email.get()=='' or passwd.get()=='':
            messagebox.showerror('Error',"All Fields Are Required ")
        else:
            querry='select *from register where email=%s and password=%s'
            values = (email.get(),passwd.get())
            cur.execute(querry,values)
            data=cur.fetchone()
            if data == None:
                messagebox.showerror('Error','Invalid Email or Password')
            else:
                root.destroy()
                from Order import UI
                from PyQt5 import QtWidgets, uic
                from PyQt5 import uic
                UI()
                             
    bttn1 = Button(root,text='Register new account?',command=lambda:show_sigin(),font=("Arial",12,'bold'),\
        bd=0,bg='white',cursor='hand2')
    bttn1.place(x=260,y=365)

    bttn2 = Button(root,text='Forgotten password?',command=reset_pass,font=("Arial",12,'bold'),\
        bd=0,bg='white',cursor='hand2')
    bttn2.place(x=515,y=365)
    
    def bttn_login(x,y,text,bcolor,fcolor):
        def on_enter(e):
            my_button1['background']=bcolor
            my_button1['foreground']=fcolor
        def on_leave(e):
            my_button1['background']=fcolor
            my_button1['foreground']=bcolor
        my_button1 = Button(root,width=25,height=3,text=text,\
            fg=bcolor,bg=fcolor,border=0,activeforeground=fcolor,command=lambda:login_bttn_ok(),activebackground=bcolor,)
        my_button1.place(x=375,y=420)
        my_button1.bind('<Enter>',on_enter)
        my_button1.bind('<Leave>',on_leave)
       
    bttn_login(0,0,"Login",'#EB46CD',"#141414")

main_window()
root.resizable(False, False) 
root.mainloop()
