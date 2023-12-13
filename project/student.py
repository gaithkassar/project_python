from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from  PIL import Image,ImageTk
import mysql.connector as mc

class Student:
    def __init__(self,cf):
        self.studentFrame=Frame(cf,pady=10,padx=10)
        self.studentFrame.grid(row=0,column=1,sticky='senw',pady=5)
        self.img2=Image.open("images/images.png",mode='r',formats=None)
        self.img2.thumbnail((200,200))
        self.new_img2=ImageTk.PhotoImage(self.img2)
        self.imgStudent=Label(self.studentFrame,image=self.new_img2,padx=10,pady=10)
        self.imgStudent.pack()
        self.buttonStudent=Button(self.studentFrame,command=self.openStudentWindo,font=('tahoma',10,'bold'),text='Student Mangment ',bg='#16537e',fg='white',padx=19,pady=10)
        self.buttonStudent.pack()

    def openStudentWindo(self):
        stdw=Studentwindow()


class Studentwindow:
    def __init__(self):
        self.master=Toplevel()
        self.master.title('Student Mangment System')
        self.master.geometry('1200x600+0+0')
        ##################################################
        self.frameleft=Frame(self.master,width=400,bg="#a3d4eb")
        self.frameleft.pack(side=LEFT,fill=Y)
        ##################################################
        self.firstname=Label(self.frameleft,text='firstname',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.firstname.place(x=20,y=20)
        self.lastname=Label(self.frameleft,text='lastname',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.lastname.place(x=20,y=70)
        self.CIN=Label(self.frameleft,text='CIN',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.CIN.place(x=20,y=120)
        self.email=Label(self.frameleft,text='email',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.email.place(x=20,y=170)

        self.name=StringVar()
        self.last=StringVar()
        self.cin=StringVar()
        self.emal=StringVar()
        self.firstname=Entry(self.frameleft,text='firstname',font=('tahoma',15,'bold'),textvariable=self.name)
        self.firstname.place(x=130,y=20)
        self.lastname=Entry(self.frameleft,text='lastname',font=('tahoma',15,'bold'),textvariable=self.last)
        self.lastname.place(x=130,y=70)
        self.CIN=Entry(self.frameleft,text='CIN',font=('tahoma',15,'bold'),textvariable=self.cin)
        self.CIN.place(x=130,y=120)
        self.email=Entry(self.frameleft,text='email',font=('tahoma',15,'bold'),textvariable=self.emal)
        self.email.place(x=130,y=170)
         
        self.add=Button(self.frameleft,text="Add",command=self.add,font=('tahoma',15,'bold'),bg="#5703ff")
        self.add.place(x=20,y=250)
        self.Update=Button(self.frameleft,text="Update",command=self.Update,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Update.place(x=100,y=250)
        self.Delete=Button(self.frameleft,text="Delete",command=self.delete,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Delete.place(x=220,y=250) 
        self.Clear=Button(self.frameleft,text="clear",command=self.clear,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Clear.place(x=320,y=250) 


        ############3 right frame Star  here#################
        self.frameright=Frame(self.master,width=800)
        self.frameright.pack(side=LEFT,fill=BOTH)
        ############3 right frame End  here#################
        self.framerighttop=Frame(self.frameright,width=800)
        self.framerighttop.pack(fill=X) 

        self.searhStuden=Entry(self.framerighttop,font=('tahoma',15,'bold'),width=80)
        self.searhStuden.grid(row=0,column=1,sticky='snww',padx=10,pady=10)

        self.buttonsearch=Button(self.framerighttop,text="Search",command=self.search,font=('tahoma',15,'bold'),width=50)
        self.buttonsearch.grid(row=0,column=0,sticky='snew',padx=10,pady=10)

        self.framerighttop.grid_columnconfigure(0,weight=1)
        self.framerighttop.grid_columnconfigure(1,weight=1)

        ############### frame Tree view##############################
        self.frameview=Frame(self.frameright,bg='blue')
        self.frameview.pack(fill=BOTH)
        #لوضع شريط للاتنقل بين سجلات البيانات
        self.scrollbar=Scrollbar(self.frameview,orient=VERTICAL)
    
        self.table=ttk.Treeview(self.frameview,columns=("id","firstname","lastname","CIN","Email"),show='headings',yscrollcommand=self.scrollbar.set,height=26)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("id",text="ID")
        self.table.heading("firstname",text="firstname")
        self.table.heading("lastname",text="lastname")
        self.table.heading("CIN",text="CIN")
        self.table.heading("Email",text="Email")
         
        self.table.column("id",anchor=W,width=10)
        self.table.column("firstname",anchor=W)
        self.table.column("lastname",anchor=W)
        self.table.column("CIN",anchor=W)
        self.table.column("Email",anchor=W)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)
    #دالة الإضافة
    def add(self):
        try:
            mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
            )
            mycursor=mydb.cursor()
            sql='insert into student(firstname,lastname,CIN,Email) values (%s,%s,%s,%s)'
            if(len(self.firstname.get())==0 or len(self.lastname.get())==0 or len(self.CIN.get())==0 or len(self.email.get())==0):
                mb.showerror('Error','يجب ملئ جميع الحقول',parent=self.master)
            elif not self.firstname.get().isalpha():
                    mb.showerror('Error',' خطأ بالاسم يجب أن يكون نص',parent=self.master)
            elif not self.lastname.get().isalpha():
                    mb.showerror('Error','خطأ بالكنية يجب أن يكون نص',parent=self.master)
            elif not self.CIN.get().isdigit():
                    mb.showerror('Error',' المعرف  يجب أن يكون رقم',parent=self.master)
        
            else:
                val=(self.firstname.get(),self.lastname.get(),self.CIN.get(),self.email.get())
                mycursor.execute(sql,val)
                mydb.commit()
                mb.showinfo('successfly added','تمت الإضافة بنجاح',parent=self.master)
                self.clear()
                mydb.close()
                self.read()
        except:
             mb.showerror('Error','xampp قم بتشغيل ال',parent=self.master)
    #دالة قراء البيانات من الجدول 
    def read(self):
        try:
            mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
            )
            mycursor=mydb.cursor()
            sql='select *from student'
            mycursor.execute(sql)
            myresults=mycursor.fetchall()
            self.table.delete(*self.table.get_children())
            for re in myresults:
                self.table.insert('','end',iid=re[0],values=re)
                mydb.commit()
            mydb.close()
        except:
             mb.showerror('Error','xampp قم بتشغيل ال',parent=self.master)
    # دالة وضع البيانات بالحقول عند الضغط على سجل معين
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.last.set(val[2])
        self.cin.set(val[3])
        self.emal.set(val[4])
    #دالة تنظيف الحقول
    def clear(self):
         self.firstname.delete(0,'end')
         self.lastname.delete(0,'end')
         self.CIN.delete(0,'end')
         self.email.delete(0,'end')
    # دالة الحذف
    def delete(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        
        sql=("delete from student where id="+self.iid)
        
        mycursor.execute(sql)
        mydb.commit()
        mb.showinfo('Delete ','تم الحذف بنجاح',parent=self.master)
        self.read()
        self.clear()
    # دالة التعديل
    def Update(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        
        sql=("update student set firstname=%s,lastname=%s,CIN=%s,Email=%s  where id=%s")
        val=(self.name.get(),self.last.get(),self.cin.get(),self.emal.get(),self.iid)
        mycursor.execute(sql,val)
        mydb.commit()
        mb.showinfo('update ','تم التعديل  بنجاح',parent=self.master)
        self.read()
        self.clear()
    #دالة البحث حسب ال id
    def search(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        sql=('select *from student where id='+self.searhStuden.get())
        if not self.searhStuden.get().isdigit():
                 mb.showerror('Error','حصراً id البحث عن طريق ',parent=self.master)
        else:
            mycursor.execute(sql)
            myresults=mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('','end',iid=myresults[0],values=myresults)
            mydb.commit()
            mydb.close()

        


