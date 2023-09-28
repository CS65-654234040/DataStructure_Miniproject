from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

#สร้างหน้าต่าง Merge Sort
merge = Tk()
merge.geometry("948x550+300+150")
merge.title("Merge Sort")
merge.configure(background="gray")

#ใส่ข้อความบรรทัดแรก
text1 = Label(text="การเรียงลําดับข้อมูลแบบรวม (Merge Sorting)",fg="green",font=25)
text1.grid(row=0,column=2,columnspan=5,padx=90,pady=20)

#ข้อความ
text2 =Label(text="กรอกข้อมูล",fg="green",font=25)
text2.grid(row=1,column=2,columnspan=1)

#ช่องใส่ข้อมูล
sort = Entry(width=30,font=15)
sort.grid(row=1,column=3,columnspan=1)

#ข้อความตัวอย่าง
text3 = Label(text="ตัวอย่าง : 6 1 8 11 9",fg="black",background="gray",font=10)
text3.grid(row=2,column=3,pady=3)

button1 = Button(text="ยืนยัน", font=3)
button1.place(x=190,y=135) 
button2 = Button(text="ยกเลิก", font=3)
button2.place(x=280,y=135)


merge.mainloop()