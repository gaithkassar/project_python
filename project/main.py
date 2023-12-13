from tkinter import *
from  PIL import Image,ImageTk
import student as s
import exam as e
import library as l
import staff as t
import infoun as i
import mysql.connector as mc
import tkinter.messagebox as mb

class Unevirsty:
    def __init__(self,mast):
        self.master=mast
        self.master.title("Student Mangment System")
        self.width=self.master.winfo_screenwidth()
        self.height=self.master.winfo_screenheight()
        self.master.geometry("{w}x{h}+0+0".format(w=self.width,h=self.height))
        self.master.state('zoomed')
        ################# frame Top start Here ###########
        self.frametop=Frame(self.master,bg='#16537e',height=200)
        self.frametop.pack(fill=X)
        self.sms=Label(self.frametop,text='Sham Unevirsty  Mangment  System',bg='#16537e',fg='white',font=('tahoma',40),pady='60')
        self.sms.pack( )
       
        ################# frame Top end Here ###########
        ################# frame  Center star  Here ###########
        self.centerFrame=Frame(self.master)
        self.centerFrame.pack(fill=X)
        ################# frame center  End   Here ###########

        ################# frame Unviersty  info   Here ###########
        self.uviersityInfo=Frame(self.centerFrame,pady=10,padx=10)
        self.uviersityInfo.grid(row=0,column=0,sticky='snew',pady=5)
        self.img=Image.open("images/download.png",mode='r',formats=None)
        self.img.thumbnail((200,200))
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imguviersity=Label(self.uviersityInfo,image=self.new_img,padx=10,pady=10)
        self.imguviersity.pack()
        self.buttonuviersity=Button(self.uviersityInfo,command=self.openInfounWindo,font=('tahoma',10,'bold'),text='about Unviersty ',bg='#16537e',fg='white',padx=27,pady=10)
        self.buttonuviersity.pack()
        ################# frame student  info   Here ###########
        std=s.Student(self.centerFrame)
        ################# frame staff  info   Here ###########
        staf=t.Staff(self.centerFrame)
       
        ################# Bottom  Frame star  Here ###########
        self.bootomframe=Frame(self.master,height=200)
        self.bootomframe.pack(fill=X)
        ################# Bottom Frame  End   Here ###########

        ################# Library Frame     Here ###########
        lib=l.Library(self.bootomframe)
        
        ################# Exam Frame     Here ###########
        exa=e.Exam(self.bootomframe)

        self.centerFrame.grid_columnconfigure(0,weight=1)
        self.centerFrame.grid_columnconfigure(1,weight=1)
        self.centerFrame.grid_columnconfigure(2,weight=1)

        self.bootomframe.grid_columnconfigure(0,weight=1)
        self.bootomframe.grid_columnconfigure(1,weight=1)
   
    def openInfounWindo(self):
        self.master=Toplevel()
        self.master.title('about  Uneviersty')
        self.master.geometry('1200x800+0+0')
        self.TileLabel=Label(self.master,text="about   Sham   Uneviersty",bg="#16537e",font=('tahoma',30,'bold'),pady=50,fg='white')
        self.TileLabel.pack(fill=X)
        self.txt=StringVar()
        self.Messagee=Message(self.master,textvariable=self.txt,justify=RIGHT,font=('tahoma',15,'bold'),width=1200)
        self.Messagee.pack(fill=X)
        
        self.opn=open("D:/tst.txt","r")
        self.txt.set(self.opn.readlines())
    
        
class Login:
    def __init__(self,window):
        self.master=window
        self.master.title("Login System")
        self.master.geometry("400x500+150+150")
        self.img=Image.open('images/download.png')
        self.img.thumbnail((500,500))
        
        self.new_img=ImageTk.PhotoImage(self.img)
        self.imguviersity=Label(self.master,image=self.new_img,padx=10,pady=10,width=500,height=300)
        
        self.imguviersity.pack()
        self.framelogin=Frame(self.master)
        self.framelogin.pack()
        self.labeluser=Label(self.framelogin,text='User name',pady=10,padx=10,font=('tahoma',13,'bold'))
        self.labeluser.grid(row=0,column=0)
        self.labelpassord=Label(self.framelogin,text='Passowrd',pady=10,padx=10,font=('tahoma',13,'bold'))
        self.labelpassord.grid(row=1,column=0)

        self.username=Entry(self.framelogin,font=('tahoma',13,'bold'))
        self.username.grid(row=0,column=1,pady=10,padx=10)

        self.passowrd=Entry(self.framelogin,font=('tahoma',13,'bold'),show='*')
        self.passowrd.grid(row=1,column=1,pady=10,padx=10)

        self.loginbutton=Button(self.framelogin,text='Login',command=self.login,font=('tahoma',13,'bold'),bg='#16537e',fg='white')
        self.loginbutton.grid(row=2,column=0,columnspan=2,sticky='snew',padx=10,pady=10)
    def login(self):
        try:
            mydb=mc.connect(
            host='localhost',
            user='root',
            password='',
            database='university'
            )
            mycursor=mydb.cursor()
            sql="select *from loginadmi where Username='"+self.username.get()+"'  and 	Passowrd='"+self.passowrd.get()+"' "
            mycursor.execute(sql)
            res=mycursor.fetchone()
            if(res==None):
                mb.showerror('Error','خطأ  باسم المستخدم أو كلمة الس',parent=self.master)
            else:
              win=Toplevel()
              window=Unevirsty(win)
        except:
             mb.showerror('Error','xampp قم بتشغيل ال',parent=self.master)
            


if(__name__=='__main__'):
    window = Tk()
    
    un=Login(window)
    mainloop()


