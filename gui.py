from tkinter import *
from aes import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.filedialog import askopenfile 
import os.path
import random
import string


root = Tk()
root.geometry("750x600")
root.title("ENCRYPTION PROGRAM") 
root.call('wm', 'iconphoto',Tk._w,ImageTk.PhotoImage(Image.open('encrypo.ico')))
root.configure(background = "light goldenrod")


def hide_frame() :                                                                                                                                                                                                                                                                                                                                                                                                                      
    first_frame.grid_forget()
    sec_frame.grid_forget()
    third_frame.grid_forget()

def send_output(key,output):
    global_text.set(output)
    global_key.set(key)

def open_file(): 
    
    ex.delete(0,END)

    file1 = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')]) 
    key=ex.get()
    
    file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))
    file2 = open('Encrypted/'+file_name+'.txt',mode='w+')
    if file1 is not None: 
        text = file1.read() 
        messagebox.showinfo("FILE CONTENT",text)
        output=aesEncrypt(text,key)
        
        messagebox.showinfo("ENCRYPTED OUTPUT",output)
        messagebox.showinfo("OUTPUT SAVED IN:",'Encrypted/'+file_name+'.txt')
        file2.write(output)
        file1.close()
        file2.close() 
    else :
        messagebox.showerror("ERROR","File is EMPTY!!")

def popup():
    
    key=e1.get()
    text=e2.get()
    name = e3.get()
    
    
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    
    
    if(text==""):
        messagebox.showerror("ERROR","Enter 16 bit text only")
    else:
        file = open('Encrypted/'+name+'.txt',"w+")
        output=aesEncrypt(text,key)
        
        messagebox.showinfo("ENCRYPTED OUTPUT",output)
        messagebox.showinfo("OUTPUT SAVED IN:",'AES-Encrption-Using-Python/Encrypted/'+name+'.txt')
        file.write(output)
        file.close()



def popdown():
    name = e4.get()
    file1 = open('Encrypted/'+name+'.txt',"r")
    file2 = open('Decrypted/'+name+'decrypted.txt','w+')
    text= file1.read()
    key=e5.get() 
    e4.delete(0,END)
    
    file1.close()
    if(text==""):
        messagebox.showerror("ERROR","Please enter valid text")
    else:
        output=aesDecrypt(text,key)
        messagebox.showinfo("DECRYPTED OUTPUT",output)
        file2.write(output)
        messagebox.showinfo('Decrypted Output saved in file : ','AES-Encrption-Using-Python/Decrypted/'+name+'decrypted.txt')
        file2.close()




def file_one():
    hide_frame()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    ex.delete(0,END)
    first_frame.grid(sticky=N+S+W+E)
    first_frame.configure(background = "light goldenrod")
    myLabel1 = Label(first_frame,text="TEXT ENCRYPTION",bg="light goldenrod",fg="OrangeRed4",font="Helvetica 20 bold ")
    myLabel2 = Label(first_frame,text="ADVANCED ENCRYPTION STANDARD",bg="light goldenrod",fg="OrangeRed4",font="Helvetica 18 bold ")
    myLabel1.grid(row=0,column=1)
    myLabel2.grid(row=1,column=1)
    
    myLabel3=Label(first_frame,text="KEY(16 char)",font="bold",bg="light goldenrod",fg="black")
    myLabel3.grid(row=3,column=0,pady=20,ipadx=10,sticky=E)
    e1.grid(row=3,column=1,pady=20)
    e1.insert(0,"")
    
    myLabel4=Label(first_frame,text="TEXT",font="bold",bg="light goldenrod",fg="black")
    myLabel4.grid(row=4,column=0,pady=20,ipadx=10,sticky=E)
    e2.grid(row=4,column=1,pady=20)
    e2.insert(0,"Enter text here")
    
    
    myLabel5=Label(first_frame,text="FILENAME",font="bold",bg="light goldenrod",fg="black")
    myLabel5.grid(row=5,column=0,pady=20,ipadx=10,sticky=E)
    e3.grid(row=5,column=1,pady=20)
    e3.insert(0,"Not required if you choose a file")
    
    encryptButton=Button(first_frame,text="Encrypt",fg="white",bg="OrangeRed4",command=popup,activeforeground="black",activebackground="coral",relief="raised",bd=9)
    encryptButton.grid(row=6,column=1)

    orLabel = Label(first_frame,text="OR",font="Helvetica 16 bold italic",bg="light goldenrod",fg="OrangeRed4")
    orLabel.grid(row=8,column=1)

    myLabel3=Label(first_frame,text="KEY(16 char)",font="bold",bg="light goldenrod",fg="black")
    myLabel3.grid(row=9,column=0,pady=20,ipadx=10,sticky=E)
    ex.grid(row=9,column=1,pady=20)
    ex.insert(0,"")

    fileButton = Button(first_frame,text="Choose a file",fg="white",bg="OrangeRed4",command=open_file,activeforeground="black",activebackground="coral",relief="raised", bd=8)
    fileButton.grid(row =10, column=1 , pady = 20)

    button_quit=Button(first_frame,text="EXIT",command=root.quit,fg="white",bg="OrangeRed4",activeforeground="black",activebackground="coral",relief="raised",bd=9)
    button_quit.grid(row=12,column=1,pady=20)


def file_two():
    hide_frame()
    sec_frame.grid(sticky=N+S+W+E)
    sec_frame.configure(background = "light goldenrod")
    
    myLabel1 = Label(sec_frame,text="TEXT DECRYPTION",bg="light goldenrod",fg="OrangeRed4",font="Helvetica 20 bold")
    myLabel2 = Label(sec_frame,text="ADVANCED ENCRYPTION STANDARD",bg="light goldenrod",fg="OrangeRed4",font="Helvetica 18 bold")
    myLabel1.grid(row=0,column=1)
    myLabel2.grid(row=1,column=1)
    
    instLabel = Label(sec_frame,text="Enter the filename situated in '~/AES-Encrption-Using-Python/Encrypted'  ",font="bold",bg="light goldenrod")
    instLabel.grid(row=3,column=1)

    fileLabel = Label(sec_frame,text="FILENAME  ",font="bold",bg="light goldenrod")
    fileLabel.grid(row=4,column=0,pady=20,ipadx=10,sticky=E)
    e4.grid(row=4,column=1,pady=40)
    
    myLabel4=Label(sec_frame,text="KEY(16 BIT)",font="bold",bg="light goldenrod")
    myLabel4.grid(row=6,column=0,pady=20,ipadx=10,sticky=E)
    e5.grid(row=6,column=1,pady=20)
    
    decryptButton=Button(sec_frame,text="Decrypt",fg="white",bg="OrangeRed4",command=popdown,activeforeground="white",activebackground="coral",relief="raised",bd=5)
    decryptButton.grid(row=9,column=1)
    
    button_quit=Button(sec_frame,text="EXIT",command=root.quit,fg="white",bg="OrangeRed4",activeforeground="white",activebackground="coral",relief="raised",bd=5)
    button_quit.grid(row=10,column=1,pady=40)

def file_three():
    hide_frame()
    third_frame.configure(background = "light goldenrod")
    third_frame.grid(sticky=N+S+W+E)
    
    picture = PhotoImage(file="pro.png")
    pictureLabel = Label(third_frame,padx=10,image=picture).grid(row=3,sticky=E)

    myLabel1 = Label(third_frame,text="VERSION 1.1",font="Helvetica 20 bold",bg="coral")
    myLabel2 = Label(third_frame,text="A SMALL ENCRYPTION PROJECT",bg="light goldenrod")
    myLabel3 = Label(third_frame,text="DONE BY-",bg="light goldenrod")
    myLabel4 = Label(third_frame,text="PIJUSH BHUYAN",bg="light goldenrod")
    myLabel5 = Label(third_frame,text="BHASKAR JYOTI BHATTACHARYA",bg="light goldenrod")
    myLabel6 = Label(third_frame,text="ARITRA KAUSHIK",bg="light goldenrod")
    myLabel7 = Label(third_frame,text="SOUVIK BARUAH",bg="light goldenrod")
    myLabel8 = Label(third_frame,text="OPEN SOURCE",font="italic 10 ",bg="light goldenrod")
    myLabel9 = Label(third_frame,text="SOME REQUIRED FILES ARE TAKEN FROM INTERNET",font="italic 10",bg="light goldenrod")
    myLabel1.grid(row=0,column=0,columnspan=2,sticky=E,pady=20)
    myLabel2.grid(row=1,column=0,sticky=W)
    myLabel3.grid(row=2,column=0,sticky=W)
    myLabel4.grid(row=4,column=0,sticky=W)
    myLabel5.grid(row=5,column=0,sticky=W)
    myLabel6.grid(row=6,column=0,sticky=W)
    myLabel7.grid(row=7,column=0,sticky=W)
    myLabel8.grid(row=8,column=0,sticky=W,pady=10)
    myLabel9.grid(row=9,column=0,sticky=W)

menubar = Menu(root)
menubar.add_command(label="ENCRYPT",activebackground="OrangeRed4",activeforeground="black",command=file_one)
menubar.add_command(label="DECRYPT",activebackground="OrangeRed4",activeforeground="black",command=file_two)
menubar.add_command(label="ABOUT",activebackground="OrangeRed4",activeforeground="black",command=file_three)
root.config(menu=menubar)
first_frame = Frame(root,width=600,height=400)
sec_frame = Frame(root,width=600,height=400)
third_frame = Frame(root,width=600,height=400)
e1 = Entry(first_frame,show='*',width=65,borderwidth=6)
e2 = Entry(first_frame,width=65,borderwidth=6)
e3 = Entry(first_frame,width=65,borderwidth=6)
ex = Entry(first_frame,show='*',width=65,borderwidth=6)
global_text=StringVar()
global_key=StringVar()
e4 = Entry(sec_frame,width=70,borderwidth=6)
e5 = Entry(sec_frame,show='*',width=70,borderwidth=6,textvariable=global_key)
file_one()
root.mainloop()