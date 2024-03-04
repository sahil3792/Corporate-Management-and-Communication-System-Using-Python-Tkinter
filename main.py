from tkinter import *
import tkinter 
from PIL import ImageTk, Image
from tkinter.ttk import *
import ttkbootstrap as ttk




window = tkinter.Tk()  # creates a Tk() object 
window.title("Skive")  # will display the Name Skive on the top
window.geometry('700x500') # defines the window size
#window.attributes('-fullscreen', True)
window.configure(bg='#393939') 
window.iconbitmap("images/Logo.ico")

def login():
    f3=Frame()
    f3.place(x=0,y=0,width=700,height=500)
    e1=Entry(f3)
    e1.pack()
    e2=Entry(f3)
    e2.pack()
    b2=Button(text="back",command=home)
    b2.pack()
    b3=Button(text="Login",command=home)
    b3.pack()

def register():
    f3=Frame()
    f3.place(x=0,y=0,width=700,height=500)
    e1=Entry(f3)
    e1.pack()
    e2=Entry(f3)
    e2.pack()
    e3=Entry(f3)
    e3.pack()
    b2=Button(text="back",command=home)
    b2.pack()
    b3=Button(text="Login",command=home)
    b3.pack()

def home():
    frame1 = tkinter.Frame(window, width=600, height=400)
    frame1.pack()
    frame1.place(anchor='e', relx=0.5, rely=0.5)
    frame1.configure(bg='#393900')

    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open("images/DisplayLogo.jpg"))


    # Create a Label Widget to display the text or Image
    label = tkinter.Label(frame1,borderwidth=0, image = img)
    label.pack()

    frame2 = tkinter.Frame(window, width=600, height=400)
    frame2.pack()
    frame2.place(anchor='w', relx=0.5, rely=0.5)
    frame2.configure(bg='#393939')

    label1 =tkinter.Label(
    frame2, 
    text = "SKIVE BRING THE \n TEAM TOGETHER\n WHEREVER YOU\n ARE", 
    borderwidth=0, 
    background="#393939", 
    foreground="#EEEEEE",
    font=("Eckhardt-headline JNL", 28))
    label1.pack()

    Button =tkinter.Button(
    frame2,
    text ="Sign In To Skive",
    command=login)
    Button.place(x=40,y=170,width=100,height=30)

    Button1=tkinter.Button(frame2,text="Register",command=register)
    Button1.pack()
home()

window.mainloop()