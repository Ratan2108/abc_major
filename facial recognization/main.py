from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
from student import student
import os
from train import train
from recoginition import recoginize

class Face_Recognition_system:
    def  __init__(self,root):
        self.root=root 
        self.root.geometry("2000x950+0+0")
        self.root.title("face recognition system")

        #first
        img=Image.open(r"facial recognization\\IMAGES\\FACE.jpg")
        img=img.resize((650,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl = Label(self.root ,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=650,height=130)

        #second
        img1=Image.open(r"facial recognization\\IMAGES\\b.jpg")
        img1=img1.resize((650,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root ,image=self.photoimg1)
        f_lbl.place(x=650,y=0,width=650,height=130)


        #third
        img2=Image.open(r"facial recognization\\IMAGES\\c.jpg")
        img2=img2.resize((650,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root ,image=self.photoimg2)
        f_lbl.place(x=1350,y=0,width=650,height=130)


        #bgimage

   
        img3=Image.open(r"facial recognization\\IMAGES\\d.jpg")
        img3=img3.resize((2000,950),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img = Label(self.root ,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=2000,height=950)


        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SOFTWARE", font=('times new roman',35,"bold"),bg="white", fg="red")
        title_lbl.place(x=10,y=0,width=1875,height=45)


        #student button

        img4=Image.open(r"facial recognization\\IMAGES\\e.jpg")
        img4=img4.resize((250,250),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1= Button(bg_img,image=self.photoimg4,command=self.student_det,cursor="hand2")
        b1.place(x=200,y=100,width=250,height=250)

        b1= Button(bg_img,text="STUDENTS DATA",command=self.student_det,cursor="hand2", font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=200,y=300,width=250,height=40)


        #detect face button

        img5=Image.open(r"facial recognization\\IMAGES\\f.png")
        img5=img5.resize((250,250),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1= Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.facedata,)
        b1.place(x=650,y=100,width=250,height=250)

        b1= Button(bg_img,text="DETECT FACE",cursor="hand2",command=self.facedata ,font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=650,y=300,width=250,height=40)

        #attendence button

        img6=Image.open(r"facial recognization\\IMAGES\\g.png")
        img6=img6.resize((250,250),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1= Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=1100,y=100,width=250,height=250)

        b1= Button(bg_img,text="ATTENDENCE",cursor="hand2", font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=1100,y=300,width=250,height=40)


        #HELP DESK

        img7=Image.open(r"facial recognization\\IMAGES\\h.jpg")
        img7=img7.resize((250,250),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1= Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1500,y=100,width=250,height=250)

        b1= Button(bg_img,text="HELP",cursor="hand2", font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=1500,y=300,width=250,height=40)


        #TRAIN BUTTON

        img8=Image.open(r"facial recognization\\IMAGES\\I.png")
        img8=img8.resize((250,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1= Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.traindata)
        b1.place(x=200,y=480,width=250,height=250)

        b1= Button(bg_img,text="TRAIN FACE",cursor="hand2",command=self.traindata, font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=200,y=680,width=250,height=40)

        #TRAIN DATA BUTTON


        img9=Image.open(r"facial recognization\\IMAGES\\fa.jpg")
        img9=img9.resize((250,250),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1= Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_image)
        b1.place(x=650,y=480,width=250,height=250)

        b1= Button(bg_img,text="FACES",cursor="hand2",command=self.open_image ,font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=650,y=680,width=250,height=40)



        #FFF

        img10=Image.open(r"facial recognization\\IMAGES\\dev.jpg")
        img10=img10.resize((250,250),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1= Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=1100,y=480,width=250,height=250)

        b1= Button(bg_img,text="DEVELOPER",cursor="hand2", font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=1100,y=680,width=250,height=40)


        #NHG

        img11=Image.open(r"facial recognization\\IMAGES\\exit.png")
        img11=img11.resize((250,250),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1= Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1500,y=480,width=250,height=250)

        b1= Button(bg_img,text="EXIT",cursor="hand2", font=('times new roman',15,"bold"),bg="dark blue", fg="white")
        b1.place(x=1500,y=680,width=250,height=40)

    def open_image(self):
        os.startfile("facial recognization\\data")


        #button function


    def student_det(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)



    def traindata(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)


    def facedata(self):
        self.new_window=Toplevel(self.root)
        self.app=recoginize(self.new_window)








    



        



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_system(root)
    root.mainloop()



         
