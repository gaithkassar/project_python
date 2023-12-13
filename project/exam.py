from tkinter import *
from  PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
class Exam:
    def __init__(self,bf):
        
        self.examFrame=Frame(bf,pady=10,padx=50)
        self.examFrame.grid(row=1,column=1,sticky='senw',pady=5)
        self.img5=Image.open("images/download.png",mode='r',formats=None)
        self.img5.thumbnail((200,200))
        self.new_img5=ImageTk.PhotoImage(self.img5)
        self.imgExam=Label(self.examFrame,image=self.new_img5,padx=10,pady=10)
        self.imgExam.pack()
        self.buttonExam=Button(self.examFrame,command=self.openexamWindo,font=('tahoma',10,'bold'),text='Exam Mangment ',bg='#16537e',fg='white',padx=27,pady=10)
        self.buttonExam.pack()
        
    def openexamWindo(self):
        ex=Examwindow()
        
class Examwindow:
    def __init__(self):
        self.master=Toplevel()
        self.master.title('Exam Mangment System')
        self.master.geometry('1200x800+0+0')
        ##################################################
        self.frameleft=Frame(self.master,width=400,bg="#a3d4eb")
        self.frameleft.pack(side=LEFT,fill=Y)
        ##################################################
        self.namelabel=Label(self.frameleft,text='Group Name',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.namelabel.place(x=20,y=20)
        self.phonelabel=Label(self.frameleft,text='Class Room',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.phonelabel.place(x=20,y=80)
        self.booklabel=Label(self.frameleft,text='techar Name',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.booklabel.place(x=20,y=140)
        self.datedLabel=Label(self.frameleft,text=' Date',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.datedLabel.place(x=20,y=200)
        self.daterLabel=Label(self.frameleft,text='Time',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.daterLabel.place(x=20,y=450)
 

        self.name=StringVar()
        self.room=StringVar()
        self.teachar=StringVar()
        self.time=StringVar()
       
        self.Namegroup=Entry(self.frameleft,text='Group Name',font=('tahoma',14,'bold'),textvariable=self.name)
        self.Namegroup.place(x=130,y=20)
        self.Room=Entry(self.frameleft,text='Class Room',font=('tahoma',15,'bold'),textvariable=self.room)
        self.Room.place(x=130,y=80)
        self.Teacher=Entry(self.frameleft,text='Techar Name',font=('tahoma',15,'bold'),textvariable=self.teachar)
        self.Teacher.place(x=130,y=140)
        self.Date=Calendar(self.frameleft,year=2021)
        self.Date.place(x=130,y=200,width=200,height=200)
        self.Time=ttk.Combobox(self.frameleft,values=["","8:00","9:00","10:00","11:00","12:00","1:00","2:00","3:00","4:00"],font=('tahoma',14,'bold'),state='readonly',textvariable=self.time)
        self.Time.place(x=130,y=450)
      
         
        self.add=Button(self.frameleft,text="Add",command=self.add,font=('tahoma',15,'bold'),bg="#5703ff")
        self.add.place(x=20,y=700)
        self.Update=Button(self.frameleft,text="Update",command=self.Update,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Update.place(x=100,y=700)
        self.Delete=Button(self.frameleft,text="Delete",command=self.delete,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Delete.place(x=220,y=700) 
        self.Clear=Button(self.frameleft,text="clear",command=self.clear,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Clear.place(x=320,y=700) 


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
    
        self.table=ttk.Treeview(self.frameview,columns=("ID","Group Name","Class Room","Techar Nam","Date","Time"),show='headings',yscrollcommand=self.scrollbar.set,height=35)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)
        
        self.table.heading("ID",text="ID")
        self.table.heading("Group Name",text="Group Name")
        self.table.heading("Class Room",text="Class Room")
        self.table.heading("Techar Nam",text="Techar Nam")
        self.table.heading("Date",text="Date")
        self.table.heading("Time",text="Time")
         
        self.table.column("ID",anchor=W,width=10)
        self.table.column("Group Name",anchor=W,width=150)
        self.table.column("Class Room",anchor=W,width=80)
        self.table.column("Techar Nam",anchor=W,width=150)
        self.table.column("Date",anchor=W,width=100)
        self.table.column("Time",anchor=W,width=100)
        self.read()
        self.table.bind("<ButtonRelease>",self.show)
    #دالة الإضافة
    def add(self):
        mydb=mc.connect(
          host='localhost',
          user='root',
          password='',
          database='university'
        )
        mycursor=mydb.cursor()
        sql='insert into exam3(Group_Name,Class_Room,Techar_Nam,Date,Time) values (%s,%s,%s,%s,%s)'
        if(len(self.Namegroup.get())==0 or len(self.Room.get())==0 or len(self.Teacher.get())==0 or len(self.Date.get_date())==0 or len(self.Time.get())==0):
            mb.showerror('Error','يجب ملئ جميع الحقول',parent=self.master)
        elif not self.Room.get().isdigit():
                 mb.showerror('Error',' رقم القاعة يجب أن يكون رقم',parent=self.master)
        elif not self.Namegroup.get().isalpha():
                 mb.showerror('Error',' خطأ بالاسم يجب أن يكون نص',parent=self.master)
        elif not self.Teacher.get().isalpha():
                 mb.showerror('Error','خطأ  باسم المعلم',parent=self.master)
        
       
        else:
            val=(self.Namegroup.get(),self.Room.get(),self.Teacher.get(),self.Date.get_date(),self.Time.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mb.showinfo('successfly added','تمت الإضافة بنجاح',parent=self.master)
            self.clear()
            mydb.close()
            self.read()
    #دالة قراء البيانات من الجدول 
    def read(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        sql='select *from exam3'
        mycursor.execute(sql)
        myresults=mycursor.fetchall()
        self.table.delete(*self.table.get_children())
        for re in myresults:
            self.table.insert('','end',iid=re[0],values=re)
            mydb.commit()
        mydb.close()
    # دالة وضع البيانات بالحقول عند الضغط على سجل معين
    def show(self,ev):
        self.iid=self.table.focus()
        alldata=self.table.item(self.iid)
        val=alldata['values']
        self.name.set(val[1])
        self.room.set(val[2])
        self.teachar.set(val[3])
        self.time.set(val[5])
    
    #دالة تنظيف الحقول
    def clear(self):
         self.Namegroup.delete(0,'end')
         self.Room.delete(0,'end')
         self.Teacher.delete(0,'end')
         self.Date.selection_clear()
         self.Time.current(0)
    # دالة الحذف
    def delete(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        
        sql=("delete from exam3 where ID="+self.iid)
        
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
        
        sql=("update exam3 set Group_Name=%s,Class_Room=%s,Techar_Nam=%s,Date=%s,Time=%s where ID=%s")
        val=(self.name.get(),self.room.get(),self.teachar.get(),self.Date.get_date(),self.time.get(),self.iid)
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
        sql=('select *from exam3 where ID='+self.searhStuden.get())
        if not self.searhStuden.get().isdigit():
                 mb.showerror('Error','حصراً id البحث عن طريق ',parent=self.master)
        else:
            mycursor.execute(sql)
            myresults=mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('','end',iid=myresults[0],values=myresults)
            mydb.commit()
            mydb.close()
