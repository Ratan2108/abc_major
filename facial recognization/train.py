from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np


class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x950+0+0")
        self.root.title("face recognition system")

        title_lbl = Label(self.root, text="TRAIN DATA SET", font=(
            'times new roman', 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=10, y=0, width=1875, height=45)

        img_top = Image.open(
            r"facial recognization\\IMAGES\\student\\train.png")
        img_top = img_top.resize((1875, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1875, height=400)

        b1 = Button(self.root, text="TRIAN DATA", command=self.train_classifier,
                    cursor="hand2", font=('times new roman', 30, "bold"), bg="blue", fg="white")
        b1.place(x=0, y=450, width=1875, height=80)

        img_bottom = Image.open(
            r"facial recognization\\IMAGES\\student\\train2.png")
        img_bottom = img_bottom.resize((1875, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=560, width=1875, height=325)

    def train_classifier(self):
        data_dir = ("facial recognization\\data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # GRAY SCALE IMAGE
            imagenp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            # C:\Users\ratan\OneDrive\Desktop\major\facial recognization\data\user.5.1.jpg

            faces.append(imagenp)
            ids.append(id)

            cv2.imshow("training", imagenp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("result", "training data completed")


if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()
