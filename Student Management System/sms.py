from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import time,ttkthemes
from tkinter import ttk,filedialog
import pymysql,pandas


# Exit functionality
def exit_frame():
    result=messagebox.askyesno('Confirm','Do you want to exit.!')
    if result:
        root.destroy()
    else:
        pass
 

# Save as excel file functionality
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newList=[]
    for index in indexing:
        content=studentTable.item(index)
        dataList=content['values']
        newList.append(dataList)
    
    table=pandas.DataFrame(newList,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successsfully')
    

# Update student functionality
def update_frame():

    def update_data():
        qry='update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
        mycursor.execute(qry,(nameEntry.get(),phoneEntry.get(),emailEntry.get()
                                    ,addressEntry.get(),genderEntry.get(),dobEntry.get(),currentDate,currentTime,idEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified',parent=update_win)
        update_win.destroy()
        show_frame()

    update_win=Toplevel()
    update_win.grab_set()
    update_win.title('Update Student')
    update_win.resizable(0,0)
    idLabel=Label(update_win,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel=Label(update_win,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=15,pady=10)

    phoneLabel=Label(update_win,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=15,pady=10)

    emailLabel=Label(update_win,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=15,pady=10)

    addressLabel=Label(update_win,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=15,pady=10)

    genderLabel=Label(update_win,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=15,pady=10)

    dobLabel=Label(update_win,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(update_win,font=('arial',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=15,pady=10)

    update__btn=ttk.Button(update_win,text='UPDATE',command=update_data)
    update__btn.grid(row=7,columnspan=2,pady=15)

    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    listData=content['values']
    idEntry.insert(0,listData[0])
    nameEntry.insert(0,listData[1])
    phoneEntry.insert(0,listData[2])
    emailEntry.insert(0,listData[3])
    addressEntry.insert(0,listData[4])
    genderEntry.insert(0,listData[5])
    dobEntry.insert(0,listData[6])



# Show student functionality
def show_frame():
    qry='select * from student'
    mycursor.execute(qry)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


# Delete student functionality
def delete_frame():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    contentId=content['values'][0]
    qry='delete from student where id=%s'
    mycursor.execute(qry,contentId)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {contentId} is deleted successsfully')
    qry='select * from student'
    mycursor.execute(qry)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


# Search student functionality
def search_frame():

    def search_data():
        qry='select * from student where id=%s or name=%s or mobile=%s or email=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(qry,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get()
                                    ,addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetch_data=mycursor.fetchall()
        for data in fetch_data:
            studentTable.insert('',END,values=data)

    search_win=Toplevel()
    search_win.grab_set()
    search_win.title('Search Student')
    search_win.resizable(0,0)
    idLabel=Label(search_win,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel=Label(search_win,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=15,pady=10)

    phoneLabel=Label(search_win,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=15,pady=10)

    emailLabel=Label(search_win,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=15,pady=10)

    addressLabel=Label(search_win,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=15,pady=10)

    genderLabel=Label(search_win,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=15,pady=10)

    dobLabel=Label(search_win,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(search_win,font=('arial',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=15,pady=10)

    search__btn=ttk.Button(search_win,text='SEARCH',command=search_data)
    search__btn.grid(row=7,columnspan=2,pady=15)


# Add student functionality
def add_frame():

    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_win)
        else:
            try:
                qry='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(qry,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get()
                                    ,addressEntry.get(),genderEntry.get(),dobEntry.get(),currentDate,currentTime))
                con.commit() 
                result=messagebox.askyesno('Date added successfully','Do you want to clean the form')

                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id is already exists',parent=add_win)
                return

            qry='select * from student'
            mycursor.execute(qry)
            fetch_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetch_data:
                dataList=list(data)
                studentTable.insert('',END,values=dataList)



    add_win=Toplevel()
    add_win.grab_set()
    add_win.title('Add Student')
    add_win.resizable(0,0)
    idLabel=Label(add_win,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,padx=15,pady=10)

    nameLabel=Label(add_win,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,padx=15,pady=10)

    phoneLabel=Label(add_win,text='Phone',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,padx=15,pady=10)

    emailLabel=Label(add_win,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,padx=15,pady=10)

    addressLabel=Label(add_win,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,padx=15,pady=10)

    genderLabel=Label(add_win,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,padx=15,pady=10)

    dobLabel=Label(add_win,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(add_win,font=('arial',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,padx=15,pady=10)

    submit__btn=ttk.Button(add_win,text='SUBMIT',command=add_data)
    submit__btn.grid(row=7,columnspan=2,pady=15)


# Database connect function
def connectDb():

    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connWin)
            return
        
        try:
            qry='create database studentManagement'
            mycursor.execute(qry)
            qry='use studentManagement'
            mycursor.execute(qry)
            qry='create table student(id int not null primary key, name varchar(30),'\
                ' mobile varchar(10), email varchar(30),address varchar(100), gender varchar(20),'\
                ' dob varchar(20), date varchar(50), time varchar(50))'
            mycursor.execute(qry)
        except:
            qry='use studentManagement'
            mycursor.execute(qry)
        messagebox.showinfo('Success','Database connected',parent=connWin)
        connWin.destroy()
        addStudentBtn.config(state=NORMAL)
        updateStudentBtn.config(state=NORMAL)
        searchStudentBtn.config(state=NORMAL)
        showStudentBtn.config(state=NORMAL)
        exportStudentBtn.config(state=NORMAL)
        deleteStudentBtn.config(state=NORMAL)



    connWin=Toplevel()
    connWin.geometry('470x250+730+230')
    connWin.title('Database Connection')
    connWin.resizable(0,0)
    connWin.grab_set()

    hostlabel=Label(connWin,text='Host Name',font=('arial',18,'bold'))
    hostlabel.grid(row=0,column=0,padx=10)
    hostEntry=Entry(connWin,font=('arial',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    userlabel=Label(connWin,text='User Name',font=('arial',18,'bold'))
    userlabel.grid(row=1,column=0,padx=10)
    userEntry=Entry(connWin,font=('arial',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordlabel=Label(connWin,text='Password',font=('arial',18,'bold'))
    passwordlabel.grid(row=2,column=0,padx=10)
    passwordEntry=Entry(connWin,font=('arial',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    dbConnectBtn=ttk.Button(connWin,text='CONNECT',command=connect)
    dbConnectBtn.grid(row=3,columnspan=2)


# Slider function
text=''
count=0

def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)


def clock():
    global currentDate,currentTime
    currentDate=time.strftime('%d/%m/%Y')
    currentTime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date : {currentDate}\nTime : {currentTime}')
    datetimeLabel.after(1000,clock)


root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+60-40')
root.resizable(0,0)
root.title('Student Management System')

datetimeLabel=Label(root,font=('arial',16,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Student Management System'
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectBtn=ttk.Button(root,text='Connect Database',command=connectDb)
connectBtn.place(x=980,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addStudentBtn=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_frame)
addStudentBtn.grid(row=1,column=0,pady=20)

searchStudentBtn=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_frame)
searchStudentBtn.grid(row=2,column=0,pady=20)

deleteStudentBtn=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_frame)
deleteStudentBtn.grid(row=3,column=0,pady=20)

updateStudentBtn=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_frame)
updateStudentBtn.grid(row=4,column=0,pady=20)

showStudentBtn=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_frame)
showStudentBtn.grid(row=5,column=0,pady=20)

exportStudentBtn=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportStudentBtn.grid(row=6,column=0,pady=20)

exitBtn=ttk.Button(leftFrame,text='Exit',width=25,command=exit_frame)
exitBtn.grid(row=7,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','email','Address',
                                              'Gender','D.O.B','Added Date','Added Time'),xscrollcommand=ScrollbarX.set,
                                              yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=studentTable.xview)
ScrollbarY.config(command=studentTable.yview)

ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('email',text='Email Address')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Mobile No',width=200,anchor=CENTER)
studentTable.column('email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=150,anchor=CENTER)
studentTable.column('Added Date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40)
style.configure('Treeview.Heading',font=('arial',14,'bold'))

studentTable.config(show='headings')

root.mainloop()
