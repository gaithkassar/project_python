from tkinter import *
from  PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector as mc
import tkinter.messagebox as mb
from tkcalendar import Calendar
class Library:
    def __init__(self,bf):
      
        self.libraryFrame=Frame(bf,pady=10,padx=50)
        self.libraryFrame.grid(row=1,column=0,sticky='senw',pady=5)
        self.img4=Image.open("images/download.png",mode='r',formats=None)
        self.img4.thumbnail((200,200))
        self.new_img4=ImageTk.PhotoImage(self.img4)
        self.imglibrary=Label(self.libraryFrame,image=self.new_img4,padx=10,pady=10)
        self.imglibrary.pack()
        self.buttonlibrary=Button(self.libraryFrame,command=self.openlibraryWindo,font=('tahoma',10,'bold'),text='Library Mangment ',bg='#16537e',fg='white',padx=27,pady=10)
        self.buttonlibrary.pack()

    def openlibraryWindo(self):
         lib=Librarywindow()

class Librarywindow:
    def __init__(self):
        self.master=Toplevel()
        self.master.title('Library Mangment System')
        self.master.geometry('1200x800+0+0')
        ##################################################
        self.frameleft=Frame(self.master,width=400,bg="#a3d4eb")
        self.frameleft.pack(side=LEFT,fill=Y)
        ##################################################
        self.namelabel=Label(self.frameleft,text='Name Student',font=('tahoma',11,'bold'),bg="#a3d4eb")
        self.namelabel.place(x=20,y=20)
        self.phonelabel=Label(self.frameleft,text='phone',font=('tahoma',11,'bold'),bg="#a3d4eb")
        self.phonelabel.place(x=20,y=80)
        self.booklabel=Label(self.frameleft,text='Book Name',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.booklabel.place(x=20,y=140)
        self.datedLabel=Label(self.frameleft,text='Delivry Date',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.datedLabel.place(x=20,y=200)
        self.daterLabel=Label(self.frameleft,text='Return Date',font=('tahoma',13,'bold'),bg="#a3d4eb")
        self.daterLabel.place(x=20,y=450)
 

        self.name=StringVar()
        self.phone=StringVar()
        self.bok=StringVar()
       

        self.nameStudent=Entry(self.frameleft,text='Name Student',font=('tahoma',14,'bold'),textvariable=self.name)
        self.nameStudent.place(x=130,y=20)
        self.phoneStudent=Entry(self.frameleft,text='Phone',font=('tahoma',15,'bold'),textvariable=self.phone)
        self.phoneStudent.place(x=130,y=80)
        self.bookEntry=Entry(self.frameleft,text='Book Name',font=('tahoma',15,'bold'),textvariable=self.bok)
        self.bookEntry.place(x=130,y=140)
        self.DelivaryDate=Calendar(self.frameleft,year=2021)
        self.DelivaryDate.place(x=130,y=200,width=200,height=200)
        self.ReturnDate=Calendar(self.frameleft,year=2021)
        self.ReturnDate.place(x=130,y=450,width=200,height=200)
      
         
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
    
        self.table=ttk.Treeview(self.frameview,columns=("id","Name","phone","Book","Delivry Date","Return Date"),show='headings',yscrollcommand=self.scrollbar.set,height=35)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("id",text="ID")
        self.table.heading("Name",text="Name")
        self.table.heading("phone",text="phone")
        self.table.heading("Book",text="Book")
        self.table.heading("Delivry Date",text="Delivry Date")
        self.table.heading("Return Date",text="Return Date")
         
        self.table.column("id",anchor=W,width=10)
        self.table.column("Name",anchor=W)
        self.table.column("phone",anchor=W)
        self.table.column("Book",anchor=W)
        self.table.column("Delivry Date",anchor=W)
        self.table.column("Return Date",anchor=W)
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
        sql='insert into library2(Studentname,Phone,Book,DelivaryDate,ReturnDate) values (%s,%s,%s,%s,%s)'
        if(len(self.nameStudent.get())==0 or len(self.phoneStudent.get())==0 or len(self.bookEntry.get())==0 or len(self.DelivaryDate.get_date())==0 or len(self.ReturnDate.get_date())==0):
            mb.showerror('Error','يجب ملئ جميع الحقول',parent=self.master)
        elif not self.phoneStudent.get().isdigit():
                 mb.showerror('Error',' رقم الهاتف يجب أن يكون رقم',parent=self.master)
        elif not self.nameStudent.get().isalpha():
                 mb.showerror('Error',' خطأ بالاسم يجب أن يكون نص',parent=self.master)
        elif not self.bookEntry.get().isalpha():
                 mb.showerror('Error','خطأ  باسم الكتاب',parent=self.master)
        
       
        else:
            val=(self.nameStudent.get(),self.phoneStudent.get(),self.bookEntry.get(),self.DelivaryDate.get_date(),self.ReturnDate.get_date())
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
        sql='select *from library2'
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
        self.phone.set(val[2])
        self.bok.set(val[3])
        
        
        
    
    #دالة تنظيف الحقول
    def clear(self):
         self.nameStudent.delete(0,'end')
         self.phoneStudent.delete(0,'end')
         self.bookEntry.delete(0,'end')
         self.DelivaryDate.selection_clear()
         self.ReturnDate.selection_clear()
    # دالة الحذف
    def delete(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        
        sql=("delete from library2 where id="+self.iid)
        
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
        
        sql=("update library2 set Studentname=%s,Phone=%s,Book=%s,DelivaryDate=%s,ReturnDate=%s where id=%s")
        val=(self.name.get(),self.phone.get(),self.bok.get(),self.DelivaryDate.get_date(),self.ReturnDate.get_date(),self.iid)
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
        sql=('select *from library2 where id='+self.searhStuden.get())
        if not self.searhStuden.get().isdigit():
                 mb.showerror('Error','حصراً id البحث عن طريق ',parent=self.master)
        else:
            mycursor.execute(sql)
            myresults=mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('','end',iid=myresults[0],values=myresults)
            mydb.commit()
            mydb.close()

        
