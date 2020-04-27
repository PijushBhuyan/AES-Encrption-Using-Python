from tkinter import *
from aes import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfile 
import os.path

def hide_frame():
    first_frame.grid_forget()
    sec_frame.grid_forget()
    third_frame.grid_forget()

def send_output(key,output):
    global_text.set(output)
    global_key.set(key)

def popup():
    
    text=e1.get()
    key=e2.get()
    name = e3.get()
    
    e1.delete(0,END)
    e2.delete(0,END)
    if(text==""):
        messagebox.showerror("ERROR","Enter 16 bit text only")
    else:
        file = open('TXTfiles/'+name,"w+")
        output=aesEncrypt(text,key)
        send_output(key,output)
        messagebox.showinfo("ENCRYPTED OUTPUT",output)
        messagebox.showinfo("OUTPUT SAVED IN:",'TXTfiles/'+name)
        file.write(output)
        file.close()



def popdown():
    name = e4.get()
    file = open('TXTfiles/'+name,"r")
    text= file.read()
    key=global_key.get() 
    e4.delete(0,END)
    #e5.delete(0,END)
    if(text==""):
        messagebox.showerror("ERROR","Enter 16 bit text only")
    else:
        output=aesDecrypt(text,key)
        messagebox.showinfo("DECRYPTED OUTPUT",output)



def file_one():
    hide_frame()
    e1.delete(0,END)
    e2.delete(0,END)
    first_frame.grid(sticky=N+S+W+E)
    myLabel1 = Label(first_frame,text="TEXT ENCRYPTION")
    myLabel2 = Label(first_frame,text="ADVANCED ENCRYPTION STANDARD")
    myLabel1.grid(row=0,column=1)
    myLabel2.grid(row=1,column=1)
    myLabel3=Label(first_frame,text="TEXT",font="bold")
    myLabel3.grid(row=2,column=0,pady=20,ipadx=10)
    e1.grid(row=2,column=1,pady=20)
    e1.insert(0,"Enter text here")
    myLabel4=Label(first_frame,text="KEY",font="bold")
    myLabel4.grid(row=3,column=0,pady=20,ipadx=10)
    e2.grid(row=3,column=1,pady=20)
    e2.insert(0,"Enter 16 bit password here here")
    myLabel5=Label(first_frame,text="FILENAME",font="bold")
    myLabel5.grid(row=4,column=0,pady=20,ipadx=10)
    e3.grid(row=4,column=1,pady=20)
    e3.insert(0,"Please add a .txt after name")
    
    myButton=Button(first_frame,text="Encrypt",fg="black",bg="yellow",command=popup,activeforeground="black",activebackground="orange",relief="raised",bd=5)
    myButton.grid(row=7,column=1)
    button_quit=Button(first_frame,text="EXIT",command=root.quit,fg="black",bg="yellow",activeforeground="black",activebackground="orange",relief="raised",bd=5)
    button_quit.grid(row=8,column=1,pady=10)


def file_two():
    hide_frame()
    sec_frame.grid(sticky=N+S+W+E)
    myLabel1 = Label(sec_frame,text="TEXT DECRYPTION")
    myLabel2 = Label(sec_frame,text="ADVANCED ENCRYPTION STANDARD")
    myLabel1.grid(row=0,column=1)
    myLabel2.grid(row=1,column=1)
    fileLabel = Label(sec_frame,text="FILENAME : ",font="bold")
    fileLabel.grid(row=3,column=0,pady=20,ipadx=10)
    e4.grid(row=3,column=1,pady=20)
    #myLabel3=Label(sec_frame,text="TEXT",font="bold")
    #myLabel3.grid(row=4,column=0,pady=20,ipadx=10)
    #e5.grid(row=4,column=1,pady=20)
    myLabel4=Label(sec_frame,text="KEY",font="bold")
    myLabel4.grid(row=5,column=0,pady=20,ipadx=10)
    e6.grid(row=5,column=1,pady=20)
    myButton=Button(sec_frame,text="Decrypt",fg="black",bg="yellow",command=popdown,activeforeground="black",activebackground="orange",relief="raised",bd=5)
    myButton.grid(row=6,column=1)
    button_quit=Button(sec_frame,text="EXIT",command=root.quit,fg="black",bg="yellow",activeforeground="black",activebackground="orange",relief="raised",bd=5)
    button_quit.grid(row=7,column=1,pady=10)

def file_three():
    hide_frame()
    third_frame.grid(sticky=N+S+W+E)
    myLabel1 = Label(third_frame,text="VERSION 1.1",font="bold")
    myLabel2 = Label(third_frame,text="A SMALL ENCRYPTION PROJECT")
    myLabel3 = Label(third_frame,text="DONE BY-")
    myLabel4 = Label(third_frame,text="PIJUSH BHUYAN")
    myLabel5 = Label(third_frame,text="BHASKAR JYOTI BHATTACHARYA")
    myLabel6 = Label(third_frame,text="ARITRA KAUSHIK")
    myLabel7 = Label(third_frame,text="SOUVIK BARUAH")
    myLabel8 = Label(third_frame,text="OPEN SOURCE",font="italic 10 ")
    myLabel9 = Label(third_frame,text="SOME REQUIRED FILES ARE TAKEN FROM INTERNET",font="italic 10")
    myLabel1.grid(row=0,column=0,columnspan=2,sticky=E,pady=20)
    myLabel2.grid(row=1,column=0,sticky=W)
    myLabel3.grid(row=2,column=0,sticky=W)
    myLabel4.grid(row=3,column=0,sticky=W)
    myLabel5.grid(row=4,column=0,sticky=W)
    myLabel6.grid(row=5,column=0,sticky=W)
    myLabel7.grid(row=6,column=0,sticky=W)
    myLabel8.grid(row=7,column=0,sticky=W,pady=10)
    myLabel9.grid(row=8,column=0,sticky=W)



root = Tk()
root.geometry("600x400")
root.title("ENCRYPTION PROGRAM") 
root.call('wm', 'iconphoto',Tk._w,ImageTk.PhotoImage(Image.open('POWER.ico')))
menubar = Menu(root)
menubar.add_command(label="ENCRYPT",activebackground="orange",activeforeground="black",command=file_one)
menubar.add_command(label="DECRYPT",activebackground="orange",activeforeground="black",command=file_two)
menubar.add_command(label="ABOUT",activebackground="orange",activeforeground="black",command=file_three)
root.config(menu=menubar)
first_frame = Frame(root,width=600,height=400)
sec_frame = Frame(root,width=600,height=400)
third_frame = Frame(root,width=600,height=400)
e1 = Entry(first_frame,width=50,borderwidth=6)
e2 = Entry(first_frame,width=50,borderwidth=6)
e3 = Entry(first_frame,width=50,borderwidth=6)
global_text=StringVar()
global_key=StringVar()
e4 = Entry(sec_frame,width=50,borderwidth=6)
#e5 = Entry(sec_frame,width=50,borderwidth=6,textvariable=global_text)
e6 = Entry(sec_frame,width=50,borderwidth=6,textvariable=global_key)
file_one()


root.mainloop() 
