from tkinter import*
from tkinter import messagebox

window = Tk() #ประกาศตัวแปร,สร้าง window
window.geometry("600x500+250+100")#ปรับขนาดหน้าต่าง window
window.title("โปรแกรมคำนวณอย่างง่าย")#เปลี่ยนชื่อของ window
window.configure(background="lightgreen")#เปลี่ยนสี background

bg = PhotoImage(file="C:/CS65/654234040/python/1.png")#ประกาศตัวแปร,เรียกใช้ไฟล์รรูปภาพ
label = Label(window,image=bg)#ประกาศ label , สั่งให้รูปแสดงที่ window
label.pack(expand=YES)#แสดงผลในหน้าต่าง window,ปรับตำแหน่งไว้กลางจอ

def circle():
    windowcir = Toplevel(window)
    windowcir.geometry("400x300")
    windowcir.title("วงกลม")
    windowcir.configure(background="lightblue")

    def menuClear():
        radioVar.set(0)
        raduis.set("")
        result.set("")

    def menuCal():
        rdVar = raduis.get() #รับค่าที่ตัวแปรรับมาจากกล่องรับ
        try:
            rdfloat = float(rdVar) #แปรค่าตัวแปรให้เป็น Float
            if radioVar.get() == 1:
                resultCircle = 2*3.1414*rdfloat
            elif radioVar.get() == 2:
                resultCircle = 3.1414*rdfloat*rdfloat
            else:
                messagebox.showinfo(title="Information",message="กรุณาเลือกคำสั่ง")
            result.set(resultCircle)
        except ValueError:
            messagebox.showerror(title="Error",message="กรุณาป้อนค่ารัศมี")


    #Place=วางแบบสามารถกำหนด X,Y ได้ , pack=แสดงปกติ , grid=แบ่งเป็นช่องตาราง
    t1 = Label(windowcir,text="โปรแกรมคำนวณสำหรับวงกลม",font=25,fg="blue",bg="lightblue")
    t1.grid(row=0,column=0,columnspan=5,padx=90,pady=20)# columnspan=ทำให้คอลัมรวมเป็นช่องเดียวกัน,padx,pany=ไม่ให้แกนX ติดกับจอ window
    
    #ช่องรัศมี V V V
    t2 = Label(windowcir,text="รัศมี",font=20,fg="black",bg="lightblue")
    t2.grid(row=1,column=0,columnspan=2,padx=45,pady=0)
    raduis = StringVar()
    raduis.set("")
    tcircle = Entry(windowcir,font=2,fg="red",textvariable=raduis) #Entry=สร้างกล่องใส่ข้อความ
    tcircle.grid(row=1,column=1,columnspan=4)

    #ปุ่มแบบแบบเลือก
    radioVar = IntVar()#มีชนิดเป็นint ประกาศรับค่าเพื่อการเลือก (ใช้กับ tkinter)
    radioVar.set(0) #ใช้ค่าเริ่มต้นเป็น 0 
    radio1 = Radiobutton(windowcir,text="เส้นรอบวง",font=2,bg="lightblue",variable=radioVar,value=1)#Radiobutton คือ ปุ่มแบบเลือก ,variable= ผู้กับตัวแปร,value=ใส่ค่าเพื่อเปลี่ยนการเลือก
    radio1.grid(row=2,column=1,columnspan=3)
    radio2 = Radiobutton(windowcir,text="พื้นที่วงกลม",font=2,bg="lightblue",variable=radioVar,value=2)#value = ใส่ค่าเพื่อเปลี่ยนค่าตัวเลือก
    radio2.grid(row=3,column=1,columnspan=3)

    #ช่องผลลัพธ์
    result = Label(windowcir,text="ผลลัพธ์",font=20,fg="black",bg="lightblue")
    result.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
    result = StringVar()
    result.set("")
    tcircle = Entry(windowcir,font=2,fg="red",textvariable=result) #Entry=สร้างกล่องใส่ข้อความ
    tcircle["state"] = "readonly"
    tcircle.grid(row=4,column=1,columnspan=4,padx=1,pady=1)

    #ปุ่มกด
    ปุ่ม = Button(windowcir,text="คำนวณ",font=2,fg="black",command=menuCal)
    ปุ่ม.grid(row=5,column=1,columnspan=3)

    ยกเลิก = Button(windowcir,text="ยกเลิก",font=2,fg="black",command=menuClear)
    ยกเลิก.grid(row=5,column=2,columnspan=3)
    
    windowcir.mainloop()

def menuExit():  #ประกาศฟังก์ชั่นคำสั่งออก
    window.destroy() #คำสั่งทำลายตัวเอง,ปิด

def menuInfo(): #ประกาศฟังก์ชั่นแสดงข้อมูล
    windowInfo = Toplevel(window) #สร้างหน้าต่างแยก
    windowInfo.geometry("800x600+250+100")
    windowInfo.title("ผู้จัดทำ")
    windowInfo.configure(background="black")

    label1=Label(windowInfo,text="ผู้จัดทำ",font=25,fg="white",bg="black") #เขียนข้อความลงในหน้าต่าง (บน)
    label1.pack()

    bgInfo = PhotoImage(file="C:/CS65/654234040/python/3.png")
    labelInfo = Label(windowInfo,image=bgInfo)
    labelInfo.pack(expand=YES) #ปรับให้อยู่ตรงกลาง

    label2=Label(windowInfo,text="นายอนุศิษฎ์ ปานพิมเสน",font=25,fg="white",bg="black")#เขียนข้อความลงในหน้าต่าง (ล่าง)
    label2.pack()
    label3=Label(windowInfo,text="รหัส 654234040",font=25,fg="white",bg="black")
    label3.pack()
    label4=Label(windowInfo,text="หลักสูตรวิทยาการคอมพิวเตอร์",font=25,fg="white",bg="black")
    label4.pack()
    label5=Label(windowInfo,text="มหาวิทยาลัยราชภัฏสงขลา",font=25,fg="white",bg="black")
    label5.pack()

    windowInfo.mainloop()

menuItem = Menu(tearoff=False)#ประกาศตัวแปล menu ย่อย
menuItem.add_command(label="วงกลม",command=circle)#สั่งให้ menu ย่อยชื่อ "วงกลม" , ใส่ใน mymenu เพื่อเรียกใช้
menuItem.add_command(label="สี่เหลี่ยม")#สั่งให้ menu ย่อยชื่อ "สี่เหลี่ยม" , ใส่ใน mymenu เพื่อเรียกใช้
menuItem.add_separator()#เพิ่มเส้นแบ่งเมนูย่อย
menuItem.add_command(label="ออก",command=menuExit)#สั่งให้ menu ย่อยชื่อ "ออก" , ใส่ใน mymenu เพื่อเรียกใช้ , เรียกใช้คำสั่งการออก

myMenu = Menu()#ประกาศเพิ่มmenu
myMenu.add_cascade(label="คำนวณ",menu=menuItem)#แสดงเมนูให้เป็น "คำนวณ" , แสดงเมนูเล็กในเมนูใหญ่
myMenu.add_cascade(label="ผู้จัดทำ",command=menuInfo)#แสดงเมนูให้เป็น "ผู้จัดทำ"
window.config(menu=myMenu)#สร้างตัว menu แสดงใน Window และให้ menu แสดงตาม lebel

window.mainloop()