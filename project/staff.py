from tkinter import *
from tkinter import ttk
from  PIL import Image,ImageTk
import tkinter.messagebox as mb
import mysql.connector as mc
class Staff:
    def __init__(self,cf):
        
        self.staffFrame=Frame(cf,pady=10,padx=10)
        self.staffFrame.grid(row=0,column=2,sticky='senw',pady=5)
        self.img3=Image.open("images/download.png",mode='r',formats=None)
        self.img3.thumbnail((200,200))
        self.new_img3=ImageTk.PhotoImage(self.img3)
        self.imgstaff=Label(self.staffFrame,image=self.new_img3,padx=10,pady=10)
        self.imgstaff.pack()
        self.buttonstaff=Button(self.staffFrame,command=self.openStaffWindo,font=('tahoma',10,'bold'),text='staff Mangment ',bg='#16537e',fg='white',padx=27,pady=10)
        self.buttonstaff.pack()
    
    def openStaffWindo(self):
        staw=Staffwindowe()

class Staffwindowe:
    def __init__(self):
        self.master=Toplevel()
        self.master.title('Staff Mangment System')
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
        self.phone=Label(self.frameleft,text='phone',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.phone.place(x=20,y=230)
        self.Job=Label(self.frameleft,text='Job',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.Job.place(x=20,y=280)
        self.Certificate=Label(self.frameleft,text='Certificate',font=('tahoma',15,'bold'),bg="#a3d4eb")
        self.Certificate.place(x=20,y=320)
        

        self.name=StringVar()
        self.last=StringVar()
        self.cin=StringVar()
        self.emal=StringVar()
        self.phon=StringVar()
        self.job=StringVar()
        self.certificate=StringVar()
        self.firstnameEntry=Entry(self.frameleft,text='firstname',font=('tahoma',15,'bold'),textvariable=self.name)
        self.firstnameEntry.place(x=130,y=20)
        self.lastnameEntry=Entry(self.frameleft,text='lastname',font=('tahoma',15,'bold'),textvariable=self.last)
        self.lastnameEntry.place(x=130,y=70)
        self.CINEntry=Entry(self.frameleft,text='CIN',font=('tahoma',15,'bold'),textvariable=self.cin)
        self.CINEntry.place(x=130,y=120)
        self.emailEntry=Entry(self.frameleft,text='email',font=('tahoma',15,'bold'),textvariable=self.emal)
        self.emailEntry.place(x=130,y=170)
        self.phoneEntry=Entry(self.frameleft,text='phone',font=('tahoma',15,'bold'),textvariable=self.phon)
        self.phoneEntry.place(x=130,y=230)
        self.JobEntry=ttk.Combobox(self.frameleft,values=["","Teacher","Adray","employee"],font=('tahoma',14,'bold'),state='readonly',textvariable=self.job)
        self.JobEntry.place(x=130,y=280)
        self.Certificate=ttk.Combobox(self.frameleft,values=["","Professor Dr","Ph.D","Master's","vacation"],font=('tahoma',14,'bold'),state='readonly',textvariable=self.certificate)
        self.Certificate.place(x=130,y=330)

         
        self.add=Button(self.frameleft,text="Add",command=self.add,font=('tahoma',15,'bold'),bg="#5703ff")
        self.add.place(x=20,y=370)
        self.Update=Button(self.frameleft,text="Update",command=self.Update,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Update.place(x=100,y=370)
        self.Delete=Button(self.frameleft,text="Delete",command=self.delete,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Delete.place(x=220,y=370) 
        self.Clear=Button(self.frameleft,text="clear",command=self.clear,font=('tahoma',15,'bold'),bg="#5703ff")
        self.Clear.place(x=320,y=370) 
        


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
    
        self.table=ttk.Treeview(self.frameview,columns=("id","firstname","lastname","CIN","Email","Job","phone","Certificate"),show='headings',yscrollcommand=self.scrollbar.set,height=26)
        self.scrollbar.pack(side=RIGHT,fill=Y)
        self.scrollbar.config(command=self.table.yview)
        self.table.pack(fill=BOTH)

        self.table.heading("id",text="ID")
        self.table.heading("firstname",text="firstname")
        self.table.heading("lastname",text="lastname")
        self.table.heading("CIN",text="CIN")
        self.table.heading("Email",text="Email")
        self.table.heading("Job",text="Job")
        self.table.heading("phone",text="phone")
        self.table.heading("Certificate",text="Certificate")
         
        self.table.column("id",anchor=W,width=10)
        self.table.column("firstname",anchor=W,width=90)
        self.table.column("lastname",anchor=W,width=90)
        self.table.column("CIN",anchor=W,width=60)
        self.table.column("Email",anchor=W,width=120)
        self.table.column("Job",anchor=W,width=90)
        self.table.column("phone",anchor=W,width=90)
        self.table.column("Certificate",anchor=W,width=90)
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
        sql='insert into staff(firstname,lastname,CIN,Email,Job,phone,Certificate) values (%s,%s,%s,%s,%s,%s,%s)'
        if(len(self.firstnameEntry.get())==0 or len(self.phoneEntry.get())==0 or len(self.JobEntry.get())==0  or len(self.Certificate.get())==0 or len(self.lastnameEntry.get())==0 or len(self.CINEntry.get())==0 or len(self.emailEntry.get())==0):
            mb.showerror('Error','يجب ملئ جميع الحقول',parent=self.master)
        elif not self.phoneEntry.get().isdigit():
                 mb.showerror('Error',' رقم الهاتف يجب أن يكون رقم',parent=self.master)
        elif not self.firstnameEntry.get().isalpha():
                 mb.showerror('Error',' خطأ بالاسم يجب أن يكون نص',parent=self.master)
        elif not self.lastnameEntry.get().isalpha():
                 mb.showerror('Error','خطأ بالكنية يجب أن يكون نص',parent=self.master)
        elif not self.CINEntry.get().isdigit():
                 mb.showerror('Error',' المعرف  يجب أن يكون رقم',parent=self.master)
        
        else:
            val=(self.firstnameEntry.get(),self.lastnameEntry.get(),self.CINEntry.get(),self.emailEntry.get(),self.JobEntry.get(),self.phoneEntry.get(),self.Certificate.get())
            mycursor.execute(sql,val)
            mydb.commit()
            mb.showinfo('successfly added','تمت الإضافة بنجاح',parent=self.master)
            mydb.close()
            self.read()
            self.clear()
    #دالة قراء البيانات من الجدول 
    def read(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        sql='select *from staff'
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
        self.last.set(val[2])
        self.cin.set(val[3])
        self.emal.set(val[4])
        self.job.set(val[5])
        self.phon.set(val[6])
        self.certificate.set(val[7])
    #دالة تنظيف الحقول
    def clear(self):
         self.firstnameEntry.delete(0,'end')
         self.lastnameEntry.delete(0,'end')
         self.CINEntry.delete(0,'end')
         self.emailEntry.delete(0,'end')
         self.JobEntry.current(0)
         self.phoneEntry.delete(0,'end')
         self.Certificate.current(0)
    
    
    # دالة الحذف
    def delete(self):
        mydb=mc.connect(
        host='localhost',
        user='root',
        password='',
        database='university'
        )
        mycursor=mydb.cursor()
        
        sql=("delete from staff where id="+self.iid)
        
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
        
        sql=("update staff set firstname=%s,lastname=%s,CIN=%s,Email=%s,Job=%s,phone=%s,Certificate=%s  where id=%s")
        val=(self.name.get(),self.last.get(),self.cin.get(),self.emal.get(),self.job.get(),self.phon.get(),self.certificate.get(),self.iid)
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
        sql=('select *from staff where id='+self.searhStuden.get())
        if not self.searhStuden.get().isdigit():
                 mb.showerror('Error','حصراً id البحث عن طريق ',parent=self.master)
        else:
            mycursor.execute(sql)
            myresults=mycursor.fetchone()
            self.table.delete(*self.table.get_children())
            self.table.insert('','end',iid=myresults[0],values=myresults)
            mydb.commit()
            mydb.close()
