from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox
import pymysql
import tkinter as tk
from tkinter import font


#functionalityforleftframebutton

#exitfunction
def exit():
   result=messagebox.askyesno('confirm','Do you want to exit?')
   if result:
      window.destroy()
   else:
      pass   

   

#updatestudentfunction
def update_student():

   def update_data():
      query='update student set Name=%s,Address=%s,Dob=%s,Gender=%s,Email=%s,Phoneno=%s where Id=%s'
      mycursor.execute(query,(nameEntry.get(),addressEntry.get(),dobEntry.get(),genderEntry.get(),emailEntry.get(),phoneEntry.get(),idEntry.get()))
      con.commit()
      messagebox.showinfo('success','Updated successfully',parent=update_window)
      update_window.destroy()
      show_student()
      
   update_window=Toplevel()
   update_window.title('update student')
   update_window.grab_set()
   update_window.resizable(False,False)

   idLabel=Label(update_window,text='Id',font=('times new roman',20,'bold'))
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry=Entry(update_window,font=('times new roman',15,'bold'))
   idEntry.grid(row=0,column=1,padx=15,pady=10)
   
   nameLabel=Label(update_window,text='Name',font=('times new roman',20,'bold'))
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry=Entry(update_window,font=('times new roman',15,'bold'))
   nameEntry.grid(row=1,column=1,padx=15,pady=10)

   addressLabel=Label(update_window,text='Address',font=('times new roman',20,'bold'))
   addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   addressEntry=Entry(update_window,font=('times new roman',15,'bold'))
   addressEntry.grid(row=2,column=1,padx=15,pady=10)

   dobLabel=Label(update_window,text='DOB',font=('times new roman',20,'bold'))
   dobLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   dobEntry=Entry(update_window,font=('times new roman',15,'bold'))
   dobEntry.grid(row=3,column=1,padx=15,pady=10)

   genderLabel=Label(update_window,text='Gender',font=('times new roman',20,'bold'))
   genderLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   genderEntry=Entry(update_window,font=('times new roman',15,'bold'))
   genderEntry.grid(row=4,column=1,padx=15,pady=10)

   emailLabel=Label(update_window,text='Email',font=('times new roman',20,'bold'))
   emailLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   emailEntry=Entry(update_window,font=('times new roman',15,'bold'))
   emailEntry.grid(row=5,column=1,padx=15,pady=10)

   phoneLabel=Label(update_window,text='Phoneno',font=('times new roman',20,'bold'))
   phoneLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   phoneEntry=Entry(update_window,font=('times new roman',15,'bold'))
   phoneEntry.grid(row=6,column=1,padx=15,pady=10)

   update_student_button=ttk.Button(update_window,text='Update',command=update_data)
   update_student_button.grid(row=7,columnspan=2,padx=15)

   indexing=studentTable.focus()
   content=studentTable.item(indexing)
   listdata=content['values']
   idEntry.insert(0,listdata[0])
   nameEntry.insert(0,listdata[1])
   addressEntry.insert(0,listdata[2])
   dobEntry.insert(0,listdata[3])
   genderEntry.insert(0,listdata[4])
   emailEntry.insert(0,listdata[5])
   phoneEntry.insert(0,listdata[6])




#showfunction

def show_student():
   query='select *from student'
   mycursor.execute(query)
   fetched_data=mycursor.fetchall()
   studentTable.delete(*studentTable.get_children())
   for data in fetched_data:
       studentTable.insert('',END,values=data)

#deletefunction

def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where Id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('message',f'Id {content_id} is deleted successfuly')
    query='select *from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
       studentTable.insert('',END,values=data)
       datalist=list(data)

#searchfunction

def search_student():
   def search_data():
      query='select * from student where Id=%s or Name=%s '
      mycursor.execute(query,(idEntry.get(),nameEntry.get()))
      studentTable.delete(*studentTable.get_children())
      fetched_data=mycursor.fetchall()
      for data in fetched_data:
         studentTable.insert('',END,values=data)

#leftframesearchdetils

   search_window=Toplevel()
   search_window.title('search student')
   search_window.grab_set()
   search_window.resizable(False,False)

   idLabel=Label(search_window,text='Id',font=('times new roman',20,'bold'))
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry=Entry(search_window,font=('times new roman',15,'bold'))
   idEntry.grid(row=0,column=1,padx=15,pady=10)
   
   nameLabel=Label(search_window,text='Name',font=('times new roman',20,'bold'))
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry=Entry(search_window,font=('times new roman',15,'bold'))
   nameEntry.grid(row=1,column=1,padx=15,pady=10)

   addressLabel=Label(search_window,text='Address',font=('times new roman',20,'bold'))
   addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   addressEntry=Entry(search_window,font=('times new roman',15,'bold'))
   addressEntry.grid(row=2,column=1,padx=15,pady=10)

   dobLabel=Label(search_window,text='DOB',font=('times new roman',20,'bold'))
   dobLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   dobEntry=Entry(search_window,font=('times new roman',15,'bold'))
   dobEntry.grid(row=3,column=1,padx=15,pady=10)

   genderLabel=Label(search_window,text='Gender',font=('times new roman',20,'bold'))
   genderLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   genderEntry=Entry(search_window,font=('times new roman',15,'bold'))
   genderEntry.grid(row=4,column=1,padx=15,pady=10)

   emailLabel=Label(search_window,text='Email',font=('times new roman',20,'bold'))
   emailLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   emailEntry=Entry(search_window,font=('times new roman',15,'bold'))
   emailEntry.grid(row=5,column=1,padx=15,pady=10)

   phoneLabel=Label(search_window,text='Phoneno',font=('times new roman',20,'bold'))
   phoneLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   phoneEntry=Entry(search_window,font=('times new roman',15,'bold'))
   phoneEntry.grid(row=6,column=1,padx=15,pady=10)

   search_student_button=ttk.Button(search_window,text='Search Student',command=search_data)
   search_student_button.grid(row=7,columnspan=2,padx=15)

#addstudentfunction

def add_student():
   def add_data():
      if idEntry.get()=='' or nameEntry.get()=='' or addressEntry.get()=='' or dobEntry.get()=='' or genderEntry.get()=='' or emailEntry.get()=='' or phoneEntry.get()=='':
         messagebox.showerror('error','All Feilds are required',parent=add_window)
      else:
         query='insert into student values(%s,%s,%s,%s,%s,%s,%s)'
         mycursor.execute(query,(idEntry.get(),nameEntry.get(),addressEntry.get(),dobEntry.get(),genderEntry.get(),emailEntry.get(),phoneEntry.get()))
         con.commit()
         result=messagebox.askyesno('Data added succefully. Do you want clean the form?')
         if result:
            idEntry.delete(0,END)
            nameEntry.delete(0,END)
            addressEntry.delete(0,END)
            dobEntry.delete(0,END)
            genderEntry.delete(0,END)
            emailEntry.delete(0,END)
            phoneEntry.delete(0,END)
         else:
            pass
   
         query='select *from student'
         mycursor.execute(query)
         fetched_data=mycursor.fetchall()
         studentTable.delete(*studentTable.get_children())
         for data in fetched_data:
            datalist=list(data)
            studentTable.insert('',END,values=datalist)   

 #leftframeaddstudententdetails

   add_window=Toplevel()
   add_window.grab_set()
   add_window.resizable(False,False)

   idLabel=Label(add_window,text='Id',font=('times new roman',20,'bold'))
   idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
   idEntry=Entry(add_window,font=('times new roman',15,'bold'))
   idEntry.grid(row=0,column=1,padx=15,pady=10)
   
   nameLabel=Label(add_window,text='Name',font=('times new roman',20,'bold'))
   nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
   nameEntry=Entry(add_window,font=('times new roman',15,'bold'))
   nameEntry.grid(row=1,column=1,padx=15,pady=10)

   addressLabel=Label(add_window,text='Address',font=('times new roman',20,'bold'))
   addressLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
   addressEntry=Entry(add_window,font=('times new roman',15,'bold'))
   addressEntry.grid(row=2,column=1,padx=15,pady=10)

   dobLabel=Label(add_window,text='DOB',font=('times new roman',20,'bold'))
   dobLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
   dobEntry=Entry(add_window,font=('times new roman',15,'bold'))
   dobEntry.grid(row=3,column=1,padx=15,pady=10)

   genderLabel=Label(add_window,text='Gender',font=('times new roman',20,'bold'))
   genderLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
   genderEntry=Entry(add_window,font=('times new roman',15,'bold'))
   genderEntry.grid(row=4,column=1,padx=15,pady=10)

   emailLabel=Label(add_window,text='Email',font=('times new roman',20,'bold'))
   emailLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
   emailEntry=Entry(add_window,font=('times new roman',15,'bold'))
   emailEntry.grid(row=5,column=1,padx=15,pady=10)

   phoneLabel=Label(add_window,text='Phoneno',font=('times new roman',20,'bold'))
   phoneLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
   phoneEntry=Entry(add_window,font=('times new roman',15,'bold'))
   phoneEntry.grid(row=6,column=1,padx=15,pady=10)

   add_student_button=ttk.Button(add_window,text='Add Student',command=add_data)
   add_student_button.grid(row=7,columnspan=2,padx=15)

#databasefunctinalityandtablecreation
   
def connect_database():
    def connect():
        global mycursor,con
        try:
         con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
         mycursor=con.cursor()
         
        except:
           messagebox.showerror('error','Invalid Details',parent=connectwindow)
           return
        try:
           query='create database studentmanagementsystem'
           mycursor.execute(query)
           query='use studentmanagementsystem'
           mycursor.execute(query)   
           query='create table student(Id int , Name varchar(30),Address varchar(100),Dob varchar(20),Gender varchar(20),Email varchar(40),Phoneno varchar(12))'
           mycursor.execute(query)
        except:
           query='use studentmanagementsystem'
           mycursor.execute(query)  
        messagebox.showinfo('success','Database Connection is Sucessfull',parent=connectwindow)
        connectwindow.destroy()
        
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        #exportdataButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)

#databaseconnectivity

    connectwindow=Toplevel()
    connectwindow.grab_set()
    connectwindow.geometry('500x250+700+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnameLabel=Label(connectwindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)
    
    usernameLabel=Label(connectwindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)

    userEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    userEntry.grid(row=1,column=1,padx=40,pady=20)

    passwordLabel=Label(connectwindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)

    passwordEntry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)

    connectButton=ttk.Button(connectwindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

#mainwindow

window =ttkthemes.ThemedTk()
window.get_themes()
window.set_theme("blue")

window.title("Student Management System")

# Set the size, position, and resizing properties of the window
window.geometry('1174x680+50+20')
window.resizable(0, 0)

# Define the styled title text and font
title_text = "Student Management System"
title_font = font.Font(family="Helvetica", size=25, weight="bold")  # Customize font here

# Create a Label widget to display the title
title_label = tk.Label(window, text=title_text, font=title_font,fg="darkblue",padx=10,pady=10)
title_label.pack(fill=tk.X)  # Fill horizontally and add padding around the label  


connectButton=ttk.Button(window,text='connect database',command=connect_database)
connectButton.place(x=950,y=20)

#leftframecreation

leftFrame=Frame(window)
leftFrame.place(x=50,y=80,width=300,height=600)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

#exportdataButton=ttk.Button(leftFrame,text='Exportdata',width=25,state=DISABLED)
#exportdataButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=exit)
exitButton.grid(row=7,column=0,pady=20)

#rightframecreation

rightFrame=Frame(window)
rightFrame.place(x=350,y=80,width=820,height=500)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

#treeviewstudentatble

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Address','DOB','Gender','Email','Phoneno'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)
 
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM,fil=X)
scrollBarY.pack(side=RIGHT,fil=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Address',text='Address')
studentTable.heading('DOB',text='DOB')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Email',text='Email')
studentTable.heading('Phoneno',text='Phoneno')

studentTable.column('Id',width=100,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Address',width=200,anchor=CENTER)
studentTable.column('DOB',width=200,anchor=CENTER)
studentTable.column('Gender',width=200,anchor=CENTER)
studentTable.column('Email',width=200,anchor=CENTER)
studentTable.column('Phoneno',width=200,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',14))
style.configure('Treeview.Heading',font=('arial',18,'bold'))


studentTable.config(show='headings')

window.mainloop()