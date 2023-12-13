from tkinter import *
from  PIL import Image,ImageTk
        
class Infowindow:
    def ___init__(self):
        self.master=Toplevel()
        self.master.title('about  Uneviersty')
        self.master.geometry('1200x800+0+0')
        self.TileLabel=Label(self.master,text="FSM")
        self.TileLabel.pack()