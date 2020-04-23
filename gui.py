from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.geometry("600x400")
root.title("ENCRYPTION PROGRAM") 
root.call('wm', 'iconphoto',Tk._w,ImageTk.PhotoImage(Image.open('POWER.ico')))
##
myLabel1 = Label(root,text="TEXT ENCRYPTION")
myLabel2 = Label(root,text="ADVANCED ENCRYPTION STANDARD")
myLabel1.grid(row=0,column=1)
myLabel2.grid(row=1,column=1)
##
Label(root,text="TEXT",font="bold").grid(row=5,column=0,pady=40,ipadx=30)
e1 = Entry(root,width=50,borderwidth=6)
e1.grid(row=5,column=1,pady=40)
e1.insert(0,"Enter text here")
Label(root,text="KEY",font="bold").grid(row=6,column=0,pady=40,ipadx=30)
e2 = Entry(root,width=50,borderwidth=6)
e2.grid(row=6,column=1,pady=40)
e2.insert(0,"Enter text here")
##
def popup():
    messagebox.showerror("TEXT WILL BE HERE","HEllo")
##
myButton=Button(root,text="encrpt",fg="red",bg="white",command=popup,activeforeground="white",activebackground="black",relief="raised",bd=5)
myButton.grid(row=7,column=1)
button_quit=Button(root,text="exit program",command=root.quit,fg="red",bg="white",activeforeground="white",activebackground="black",relief="raised",bd=5)
button_quit.grid(row=8,column=1,pady=10)
##
root.mainloop()
