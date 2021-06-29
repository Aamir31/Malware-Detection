from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pymysql
from sandbox_model import Malware_Detection
from classification import MalwareClassification
# ---------------------------------------------------------------Login Function --------------------------------------

def close():
    win.destroy()


def login():
    if user_name.get() == "" or password.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=win)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="A@mir1122", database="fyp")
            cur = con.cursor()

            cur.execute("select * from malware where username = %s and password = %s",
                        (user_name.get(), password.get()))
            row = cur.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=win)
                close()
                dashboard()
            con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)


# ---------------------------------------------------------------End Login Function ---------------------------------

# ---------------------------------------------------- DashBoard Panel -----------------------------------------

def dashboard():

 win = Tk()
 win.title('Malware Detection')
 win.geometry('530x550')
 win.resizable(False, False)
 win.configure(background="#272736")
 win.iconbitmap('images/icon.ico')
 img = Image.open('images/pic.png')
 win.tkimage = ImageTk.PhotoImage(img)
 Label(win, image=win.tkimage, bg="#272736").place(x=-10, y=-120, relwidth=1, relheight=1)
 malware_btn = Button(win, text='Detect Malware', width=14, bg='grey', fg='black', command=Malware_Detection)
 malware_btn.place(x=100, y=320)
 classify_btn = Button(win, text='Classification', width=14, bg='grey', fg='black', command = MalwareClassification)
 classify_btn.place(x=330, y=320)
 feature_btn = Button(win, text='Feature Extraction', width=14, bg='grey', fg='black')
 feature_btn.place(x=100, y=420)
 btn = Button(win, text='Preprocessing', width=14, bg='grey', fg='black')
 btn.place(x=330, y=420)

 Logout_btn = Button(win, text='Logout', width=8, bg='grey', fg='black', command=logout)
 Logout_btn.place(x=240, y=510)


def logout():
        MsgBox = tk.messagebox.askquestion('Logout Application', 'Are you sure you want to logout?', icon='warning')
        if MsgBox == 'yes':
            win.destroy()


# -----------------------------------------------------End Deshboard Panel ---------------------------------
# ----------------------------------------------------------- Signup Window ---------------------------------------

def signup():
    # signup database connect
    def action():
        if first_name.get() == "" or last_name.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=win)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="A@mir1122", database="fyp")
                cur = con.cursor()
                cur.execute("select * from malware where username=%s", user_name.get())
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User Name Already Exits", parent=win)
                else:
                    cur.execute(
                        "insert into malware(name,username,email,password) values(%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            user_name.get(),
                            password.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=win)
                    switch()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to : {str(es)}", parent=win)

    # close signup function
    def switch():
        winsignup.destroy()


    # start Signup Window

    winsignup = Tk()
    winsignup.title("Malware Detecton")
    winsignup.resizable(False, False)
    winsignup.geometry("500x500")
    winsignup.configure(background="#272736")
    winsignup.iconbitmap('images/icon.ico')
    # heading label
    heading = Label(winsignup, text="Signup Here", width=20, font=("bold", 20), bg="#272736", fg='grey')
    heading.place(x=90, y=50)

    # form data label
    first_name = Label(winsignup, text="Name", width=20, font=("bold", 10), bg="#272736", fg='grey')
    first_name.place(x=65, y=130)

    last_name = Label(winsignup, text="UserName", width=20, font=("bold", 10), bg="#272736", fg='grey')
    last_name.place(x=65, y=170)

    user_name = Label(winsignup, text="Email", width=20, font=("bold", 10), bg="#272736", fg='grey')
    user_name.place(x=65, y=210)

    password = Label(winsignup, text="Password", width=20, font=("bold", 10), bg="#272736", fg='grey')
    password.place(x=65, y=250)

    very_pass = Label(winsignup, text="Confirm-Password", width=20, font=("bold", 10), bg="#272736", fg='grey')
    very_pass.place(x=65, y=290)

    # Entry Box ------------------------------------------------------------------

    Name = StringVar()
    user_name = StringVar()
    Email= StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=20, textvariable=Name)
    first_name.place(x=230, y=130)

    last_name = Entry(winsignup, width=20, textvariable=user_name)
    last_name.place(x=230, y=170)

    user_name = Entry(winsignup, width=20, textvariable=Email)
    user_name.place(x=230, y=210)

    password = Entry(winsignup, width=20, show="*", textvariable=password)
    password.place(x=230, y=250)

    very_pass = Entry(winsignup, width=20, show="*", textvariable=very_pass)
    very_pass.place(x=230, y=290)

    # button login

    btn_signup = Button(winsignup, text='Submit', width=8, bg='grey', fg='black', command=action)
    btn_signup.place(x=190, y=370)

    login_btn = Button(winsignup, text='Login', width=8, bg='grey', fg='black', command=switch)
    login_btn.place(x=280, y=370)

    winsignup.mainloop()


# ---------------------------------------------------------------------------End Singup Window------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------

win = Tk()
win.title("Malware Detection")
win.geometry("500x500")
win.resizable(False, False)
win.configure(background="#272736")
win.iconbitmap('images/icon.ico')

# heading label
heading = Label(win, text="Login Here", width=20, font=("bold", 20), bg="#272736", fg='grey')
heading.place(x=90, y=100)

username = Label(win, text="UserName", width=20, font=("bold", 10), bg="#272736", fg='grey')
username.place(x=80, y=200)

userpass = Label(win, text="Password", width=20, font=("bold", 10), bg="#272736", fg='grey')
userpass.place(x=80, y=250)

# Entry Box
user_name = StringVar()
password = StringVar()

userentry = Entry(win, width=20, textvariable=user_name)
userentry.focus()
userentry.place(x=220, y=200)

passentry = Entry(win, width=20, show="*", textvariable=password)
passentry.place(x=220, y=250)

# button login

btn_login = Button(win,text='Login', width=8, bg='grey', command=login)
btn_login.place(x=190, y=300)

# signup button

sign_up_btn = Button(win, text='Signup', width=8, bg='grey',  command=signup)
sign_up_btn.place(x=280, y=300)

win.mainloop()

# -------------------------------------------------------------------------- End Login Window ------------------------
