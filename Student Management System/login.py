from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Harish' or passwordEntry.get()=='1925':
        messagebox.showinfo('Success','Welcome')
        win.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct credentials')
       

win=Tk()
win.geometry('1200x700+0+0')
win.title('Login System ')

bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(win,image=bgImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(win,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,padx=20,pady=10)

usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0)

usernameEntry=Entry(loginFrame,font=('arial',18,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,padx=20,pady=10)

passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0)

passwordEntry=Entry(loginFrame,font=('arial',18,'bold'),bd=5,fg='royalblue',show='*')
passwordEntry.grid(row=2,column=1,padx=20,pady=10)

loginBtn=Button(loginFrame,text='Login',font=('times new roman',14,'bold'),width=15,fg='white',bg='cornflowerblue',
                activebackground='cornflowerblue',activeforeground='white',command=login)
loginBtn.grid(row=3,column=1,pady=10)

win.mainloop()