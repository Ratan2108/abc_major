from logging import exception
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector.connection import MySQLConnection
import cv2 

from mysql.connector import connection

from mysql.connector import cursor


class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("2000x950+0+0")
        self.root.title("face recognition system")

        # variable
        # "dep","course","year","sem","id","name","div","roll","gender","dob","mail","phone","add"

        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_mail = StringVar()
        self.var_add = StringVar()
        self.var_phone = StringVar()
        self.var_teacher = StringVar()

        # first
        img = Image.open(
            r"facial recognization\\IMAGES\\student\\a.jpg")
        img = img.resize((650, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=650, height=130)

        # second
        img1 = Image.open(
            r"facial recognization\\IMAGES\\student\\b.png")
        img1 = img1.resize((650, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=650, y=0, width=650, height=130)

        # third
        img2 = Image.open(
            r"facial recognization\\IMAGES\\c.jpg")
        img2 = img2.resize((650, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1350, y=0, width=650, height=130)

        # bgimage

        img3 = Image.open(
            r"facial recognization\\IMAGES\\d.jpg")
        img3 = img3.resize((2000, 950), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=2000, height=950)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            'times new roman', 35, "bold"), bg="white", fg="dark green")
        title_lbl.place(x=10, y=0, width=1875, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1875, height=800)

        # left frame

        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, BOLD))
        left_frame.place(x=10, y=10, width=875, height=700)

        img_leftframe = Image.open(
            r"facial recognization\\IMAGES\\student\\c.jpg")
        img_leftframe = img_leftframe.resize((860, 130), Image.ANTIALIAS)
        self.photoimg_leftframe = ImageTk.PhotoImage(img_leftframe)

        f_lbl = Label(left_frame, image=self.photoimg_leftframe)
        f_lbl.place(x=5, y=0, width=860, height=130)

        # current_course
        left_frame1 = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Current Course Information", font=("times new roman", 12, BOLD))
        left_frame1.place(x=10, y=135, width=850, height=125)

        # department
        dep_label = Label(left_frame1, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10)

        dep_combo = ttk.Combobox(left_frame1, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), width=17, state="read only")
        dep_combo["values"] = ("Select Department","Computer Science", "IT", "EC", "Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10)

        # course
        course_label = Label(left_frame1, text="Course Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=3, padx=10, sticky=W)

        course_combo = ttk.Combobox(left_frame1, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), width=17, state="read only")
        course_combo["values"] = ("Select Course", "FE", "ST", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=4, padx=2, pady=10, sticky=W)

        # year

        year_label = Label(left_frame1, text="Year", font=(
            "times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(left_frame1, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), width=17, state="read only")
        year_combo["values"] = ("Select year", "2018",
                                "2019", "2020", "2021", "2022")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester

        semester_label = Label(left_frame1, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")
        semester_label.grid(row=1, column=3, padx=10, sticky=W)

        semester_combo = ttk.Combobox(left_frame1, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), width=17, state="read only")
        semester_combo["values"] = ("Select Semester", "sem-1", "sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=4, padx=2, pady=10, sticky=W)

        # Class_Student_Information
        Class_Student_Information = LabelFrame(
            left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, BOLD))
        Class_Student_Information.place(x=10, y=275, width=850, height=375)

        # student id
        student_id_label = Label(Class_Student_Information, text="Student Id :", font=(
            "times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, sticky=W)

        studentid_entry = ttk.Entry(Class_Student_Information, textvariable=self.var_id, width=20, font=(
            "times new roman", 12, "bold"))
        studentid_entry.grid(row=0, column=1, padx=10, sticky=W)

        # student Name
        student_Name_label = Label(Class_Student_Information, text="Student Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        student_Name_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        studentname_entry = ttk.Entry(Class_Student_Information, width=20,
                                      textvariable=self.var_name, font=("times new roman", 12, "bold"))
        studentname_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # CLASS DIVISION
        class_div_label = Label(Class_Student_Information, text="Division :", font=(
            "times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        # class_div_entry = ttk.Entry(Class_Student_Information, width=20,
         #                           textvariable=self.var_div, font=("times new roman", 12, "bold"))
        # class_div_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        Div_combo = ttk.Combobox(Class_Student_Information, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), width=18, state="read only")
        Div_combo["values"] = ("Select Divison", "A", "B", "C")
        Div_combo.current(0)
        Div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # roll no.
        rollno_label = Label(Class_Student_Information, text="Roll No. :", font=(
            "times new roman", 12, "bold"), bg="white")
        rollno_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        rollno_entry = ttk.Entry(Class_Student_Information, width=20,
                                 textvariable=self.var_roll, font=("times new roman", 12, "bold"))
        rollno_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # gender
        gender_label = Label(Class_Student_Information, text="Gender :", font=(
            "times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        gender_combo = ttk.Combobox(Class_Student_Information, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), width=18, state="read only")
        gender_combo["values"] = ("MALE", "FEMALE", "OTHER")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # dob
        dob_label = Label(Class_Student_Information, text="DOB :", font=(
            "times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        dob_entry = ttk.Entry(Class_Student_Information, width=20,
                              textvariable=self.var_dob, font=("times new roman", 12, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # email
        email_label = Label(Class_Student_Information, text="E-MAIL :",
                            font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        email_entry = ttk.Entry(Class_Student_Information, width=20,
                                textvariable=self.var_mail, font=("times new roman", 12, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # PhoneNo
        PhoneNo_label = Label(Class_Student_Information, text="PhoneNo.:", font=(
            "times new roman", 12, "bold"), bg="white")
        PhoneNo_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        PhoneNo_entry = ttk.Entry(Class_Student_Information, width=20,
                                  textvariable=self.var_phone, font=("times new roman", 12, "bold"))
        PhoneNo_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        Address_label = Label(Class_Student_Information, text="Address :", font=(
            "times new roman", 12, "bold"), bg="white")
        Address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        Address_entry = ttk.Entry(Class_Student_Information, width=20,
                                  textvariable=self.var_add, font=("times new roman", 12, "bold"))
        Address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher
        Teacher_label = Label(Class_Student_Information, text="Teacher Name :", font=(
            "times new roman", 12, "bold"), bg="white")
        Teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        Teacher_entry = ttk.Entry(Class_Student_Information, width=20,
                                  textvariable=self.var_teacher, font=("times new roman", 12, "bold"))
        Teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # RADIOBUTTON photo
        self.var_radio1 = StringVar()
        radio_btn1 = ttk.Radiobutton(
            Class_Student_Information, variable=self.var_radio1, text="Take Photo Sample", value="yes")
        radio_btn1.grid(row=6, column=0)

        radio_btn2 = ttk.Radiobutton(
            Class_Student_Information, variable=self.var_radio1, text="No Photo Sample", value="no")
        radio_btn2.grid(row=6, column=1)

        # BUTON FRAME

        btn_frame = Frame(Class_Student_Information,
                          border=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=230, width=800, height=40)

        # save button

        save_btn = Button(btn_frame, text="SAVE", command=self.add_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="UPDATE",  command=self.update_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        del_btn = Button(btn_frame, text="DELETE", command=self.delete_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        del_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="RESET", command=self.reset_data, width=16, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        photobtn_frame = Frame(Class_Student_Information,
                               border=2, relief=RIDGE, bg="white")
        photobtn_frame.place(x=10, y=280, width=800, height=40)

        samplephoto_btn = Button(photobtn_frame, text="Take Photo",command=self.generate_dataset, width=33, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        samplephoto_btn.grid(row=0, column=4)

        updatepho_btn = Button(photobtn_frame, text="Update Photo", width=33, font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        updatepho_btn.grid(row=0, column=7)

        # right_frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="student details", font=("times new roman", 12, BOLD))
        right_frame.place(x=950, y=10, width=875, height=700)

        img_rightframe = Image.open(
            r"facial recognization\\IMAGES\\student\\e.jpg")
        img_rightframe = img_rightframe.resize((860, 130), Image.ANTIALIAS)
        self.photoimg_rightframe = ImageTk.PhotoImage(img_rightframe)

        f_lbl = Label(right_frame, image=self.photoimg_rightframe)
        f_lbl.place(x=5, y=0, width=860, height=130)

        # search

        Search_Information = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                        text="Search Information", font=("times new roman", 12, BOLD))
        Search_Information.place(x=10, y=135, width=855, height=75)

        search_label = Label(Search_Information, text="Search By", font=(
            "times new roman", 12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_Information, font=(
            "times new roman", 12, "bold"), width=17, state="read only")
        search_combo["values"] = ("Select ", "Roll no. ", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # BLANK TEXT AREA
        search_entry = ttk.Entry(
            Search_Information, width=16, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        # BUTTON SEARCH
        search_btn = Button(Search_Information, text="SEARCH", width=16, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=2)
        # BUTTON SHOW ALLL
        showall_btn = Button(Search_Information, text="SHOW ALL", width=16, font=(
            "times new roman", 10, "bold"), bg="blue", fg="white")
        showall_btn.grid(row=0, column=4, padx=2)

        Table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=10, y=240, width=855, height=400)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(Table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll",
                                          "gender", "dob", "mail", "phone", "add", "teacher", "photo"), xscroll=scroll_x.set, yscroll=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="course")
        self.student_table.heading("year", text="year")
        self.student_table.heading("sem", text="sem")
        self.student_table.heading("id", text="id")
        self.student_table.heading("name", text="name")
        self.student_table.heading("div", text="div")
        self.student_table.heading("roll", text="roll")
        self.student_table.heading("gender", text="gender")
        self.student_table.heading("dob", text="dob")
        self.student_table.heading("mail", text="email")
        
        self.student_table.heading("add", text="address")
        self.student_table.heading("phone", text="phone no.")
        self.student_table.heading("teacher", text="teacher")
        self.student_table.heading("photo", text="photoStatus")

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("mail", width=100)
        
        self.student_table.column("add", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror("Error", "all fields are reqiure", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="face")
                mycourser = conn.cursor()
                mycourser.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (


                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_mail.get(),
                                                                                                                self.var_add.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()

                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("sucess", "details added succesfully")

            except exception as es:
                messagebox.showerror(
                    "error", f"due to:{str(es)}", parent=self.root)

    # DATA FETCH TO TABLE

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="face")
        mycourser = conn.cursor()
        mycourser.execute(" select * from student")
        data = mycourser.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

            conn.commit()
        conn.close()

    # get cursor to update data
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_mail.set(data[10]),
        self.var_add.set(data[11]),
        self.var_phone.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]),

    # UPDATE

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror(
                "Error", "all fields are reqiure", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno(
                    "update", "do you want to updte data", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="face")
                    mycourser = conn.cursor()
                    mycourser.execute("UPDATE `face`.`student` SET `dep`=%s,`course`=%s,`year`=%s,`sem`=%s,`names`=%s,`div`=%s,`rollno.`=%s,`gender`=%s,`dob`=%s,`mail`=%s,`addres`=%s,`phoneno.`=%s,`teacher`=%s,`photo`=%s WHERE `id`=%s", (
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_mail.get(),
                                                                                                                
                                                                                                                self.var_add.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_id.get()
                    ))

                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "sucess", "details updated suceessfully", parent=self.root)
                
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                print (es)
                messagebox.showerror(
                    "error", f"due to:{str(es)}", parent=self.root)

# delete data
    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "ERROR", "student id require", parent=self.root)

        else:
            try:
                delete = messagebox.askyesno(
                    "student delete page", "do you want to delete", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="root", database="face")
                    mycourser = conn.cursor()
                    sql = "delete from student where id=%s"
                    val = (self.var_id.get(),)

                    mycourser.execute(sql, val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("delete", "delete data", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "error", f"due to:{str(es)}", parent=self.root)

    # reset

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Divison")
        self.var_roll.set(""),
        self.var_gender.set("MALE")
        self.var_dob.set("")
        self.var_mail.set("")
        self.var_add.set("")
        self.var_phone.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # generate data set and take photo sample

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_name.get() == "" or self.var_id == "":
            messagebox.showerror("Error", "all fields are reqiure", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="face")
                mycourser = conn.cursor()
                mycourser.execute("select * from student")
                myresult=mycourser.fetchall()
                id=0
                for x in myresult:
                    id+=1
                mycourser.execute("UPDATE `face`.`student` SET `dep`=%s,`course`=%s,`year`=%s,`sem`=%s,`names`=%s,`div`=%s,`rollno.`=%s,`gender`=%s,`dob`=%s,`mail`=%s,`addres`=%s,`phoneno.`=%s,`teacher`=%s,`photo`=%s WHERE `id`=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_mail.get(),
                                                                                                                self.var_add.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data  
                self.reset_data()
                conn.close()



                # load predefined data from open cv

                face_cascade=cv2.CascadeClassifier("C:\\Users\\ratan\\OneDrive\\Desktop\\major\\facial recognization\\haarcascade_frontalface_default.xml")
               


                def face_crop(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_cascade.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_crop=img[y:y+h,x:x+w]
                        return face_crop

                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_crop(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_crop(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="facial recognization\\data\\user."+str(id)+"."+str(img_id)+".jpg"

                        cv2.imwrite(file_name_path,face)

                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("cropped faces",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("result","generating data set completly")
            except Exception as es:
                print(es)
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
   






                




   
   




if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
