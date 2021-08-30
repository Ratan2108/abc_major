from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

from datetime import datetime



import mysql.connector
from mysql.connector.connection import MySQLConnection
 

from mysql.connector import connection

from mysql.connector import cursor


class recoginize:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x950+0+0")
        self.root.title("face recognition system")


        title_lbl = Label(self.root, text="DETECT FACE", font=(
            'times new roman', 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=10, y=0, width=1875, height=45)


        img_top = Image.open(
            r"facial recognization\\IMAGES\\student\\fa.gif")
        img_top = img_top.resize((950, 850), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=950, height=850)


        img_bottom = Image.open(
            r"facial recognization\\IMAGES\\student\\hello.jpg")
        img_bottom = img_bottom.resize((950, 850), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=1000, y=55, width=950, height=850)

        b1 = Button(f_lbl, text="FACE RECOGNITION", 
                    cursor="hand2",command=self.face_recog, font=('times new roman', 18, "bold"), bg="white", fg="black")
        b1.place(x=300, y=750, width=350, height=60)

    #attendence mark
    def mark_attendence(self,i,r,n,d):
        with open("facial recognization\\attendence.csv","r+",newline="\n")as f:
            myData_list=f.readlines()
            name_list=[]
            for line in myData_list:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                
                now = datetime.now()
                d1 = now.strftime("%m/%d/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},PRESENT")



    #main function


    def face_recog(self):
        def draw_boundary(img,classifier,scalfactor,minimumneg,color,text,clf):
            gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_img,1.3,5)
            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_img[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))


                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="face")
                mycourser = conn.cursor()

                mycourser.execute("SELECT `names` FROM `face`.`student` WHERE `id`="+str(id))
                n = mycourser.fetchone()
                n ='+'.join(n)


                mycourser.execute("SELECT `rollno.` FROM `face`.`student` WHERE `id`="+str(id))
                r = mycourser.fetchone()
                r ='+'.join(r)

                mycourser.execute("SELECT `dep` FROM `face`.`student` WHERE `id`="+str(id))
                d = mycourser.fetchone()
                d ='+'.join(d)

                mycourser.execute("SELECT `id` FROM `face`.`student` WHERE `id`="+str(id))
                i = mycourser.fetchone()
                i ='+'.join(i)


                if confidence>77:
                    cv2.putText(img,f"id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"rollno:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendence(id,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,y]
            return coord

        def recognizer(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("C:\\Users\\ratan\\OneDrive\\Desktop\\major\\facial recognization\\haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while True:
            ret,img=video_cap.read()
            img=recognizer(img,clf,faceCascade)
            cv2.imshow('welcome to recognizer',img)

            if cv2.waitKey(1)==13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = recoginize(root)
    root.mainloop()