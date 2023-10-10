from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

#สร้างหน้าต่างเมนูหลัก
window = Tk()
window.geometry("1500x745")
window.title("Sorting And Searching")
window.iconbitmap("windows.ico")

#พื้นหลังหน้าจอหลัก
bg = PhotoImage(file="winxp.png") 
label = Label(window, image=bg)
label.pack(expand=YES)

#taskbar
image1 = PhotoImage(file="task.png")
task = Button(window, image=image1,  width=1500, height=39)
task.place(x=135, y=700)

def User():
    global window1, window2, window3, window4, window5, window6
    
    #แบ้ง
    window1 = Toplevel(window)
    window1.title("หน้าต่างใหม่")
    window1.geometry("300x290+150+30")
    window1.configure(bg="gray")
    window1.iconbitmap("social.ico")

    img1 = PhotoImage(file="040.png")
    label1 = Label(window1,bg="gray",image=img1)
    label1.pack()
    text1 = Label(window1,text="ผู้จัดทำ", font=("Tahoma", 13,"bold"))
    text1.pack(expand=YES)
    text2 = Label(window1,text="User : อนุศิษฎ์ ปานพิมเสน\nPassword : 654234040\nหน้าที่ : Merge Sort", font=("Tahoma", 13,"bold"),background="gray",fg="white")
    text2.pack(expand=YES)

    #นัง
    window2 = Toplevel(window)
    window2.title("หน้าต่างใหม่")
    window2.geometry("300x290+550+30")
    window2.configure(bg="gray")
    window2.iconbitmap("social.ico")
    
    img2 = PhotoImage(file="009.png")
    label2 = Label(window2,bg="gray", image=img2)
    label2.pack()
    text3 = Label(window2,text="ผู้จัดทำ", font=("Tahoma", 13,"bold"))
    text3.pack(expand=YES)
    text4 = Label(window2,text="User ฟิรนันท์ เจ๊ะหามะ\nPassword : 654234009\nหน้าที่ : Selection Sort", font=("Tahoma", 13,"bold"),background="gray",fg="white")
    text4.pack(expand=YES)
    
    #พี 
    window3 = Toplevel(window)
    window3.title("หน้าต่างใหม่")
    window3.geometry("300x290+950+30")
    window3.configure(bg="gray")
    window3.iconbitmap("social.ico")

    img3 = PhotoImage(file="011.png")
    label3 = Label(window3,bg="gray", image=img3)
    label3.pack()
    text3 = Label(window3,text="ผู้จัดทำ", font=("Tahoma", 13,"bold"))
    text3.pack(expand=YES)
    text3 = Label(window3,text="User : สันติภาพ ไทรทอง\nPassword : 654234011\nหน้าที่ : Insertion Sort", font=("Tahoma", 13,"bold"),background="gray",fg="white")
    text3.pack(expand=YES)

    #อัง
    window4 = Toplevel(window)
    window4.title("หน้าต่างใหม่")
    window4.geometry("300x290+150+450")
    window4.configure(bg="gray")
    window4.iconbitmap("social.ico")
    
    img4 = PhotoImage(file="015.png")
    label4 = Label(window4,bg="gray", image=img4)
    label4.pack()
    text4 = Label(window4,text="ผู้จัดทำ",font=("Tahoma", 13,"bold"))
    text4.pack(expand=YES)
    text4 = Label(window4,text="User : อิรฮาน มามะ\npassword : 654234015\nหน้าที่ : Binary search", font=("Tahoma",13,"bold"),background="gray",fg="white")
    text4.pack(expand=YES)

    #อานัส
    window5 = Toplevel(window)
    window5.title("หน้าต่างใหม่")
    window5.geometry("300x290+550+450")
    window5.configure(bg="gray")
    window5.iconbitmap("social.ico")
    
    img5 = PhotoImage(file="022.png")
    label5 = Label(window5,bg="gray", image=img5)
    label5.pack()
    text5 = Label(window5,text="ผู้จัดทำ",font=("Tahoma", 13,"bold"))
    text5.pack(expand=YES)
    text5 = Label(window5,text="User : อานัส ยูโซะ\npassword : 654234022\nหน้าที่ : Sequential Search", font=("Tahoma",13,"bold"),background="gray",fg="white")
    text5.pack(expand=YES)

    #ต้น
    window6 = Toplevel(window)
    window6.title("หน้าต่างใหม่")
    window6.geometry("300x290+950+450")
    window6.configure(bg="gray")
    window6.iconbitmap("social.ico")
    
    img6 = PhotoImage(file="023.png")
    label6 = Label(window6,bg="gray", image=img6)
    label6.pack()
    text6 = Label(window6,text="ผู้จัดทำ",font=("Tahoma", 13,"bold"))
    text6.pack(expand=YES)
    text6 = Label(window6,text="User : กฤษณพงศ์ บุญประดิษฐ์\npassword : 654234023\nหน้าที่ : Bubble Sort", font=("Tahoma",13,"bold"),background="gray",fg="white")
    text6.pack(expand=YES)

    mainloop()

def close_window():
    window1.destroy()
    window2.destroy()
    window3.destroy()
    window4.destroy()
    window5.destroy()
    window6.destroy()

 
def Userfol():
    windowUsr = Toplevel()
    windowUsr.geometry("1100x613+150+120")
    windowUsr.title("USER")
    windowUsr.iconbitmap("userfolder.ico")

    bg = PhotoImage(file="user.png")
    usm = Label(windowUsr,image=bg)
    usm.pack(expand=YES)

    button1 = Button(windowUsr, text="เปิดรายชื่อ", command=User,font=("Tahoma", 13,"bold"),fg="green")
    button1.place(x=80,y=560)

    button2 = Button(windowUsr, text="ปิดรายชื่อ", command=close_window,font=("Tahoma", 13,"bold"),fg="red")
    button2.place(x=300,y=560)


    windowUsr.mainloop()

#ฟังชั่นในปุ่ม window     
def button_start():
    pass

#แบบฟองสบู่ (Bubble sort)
def bubblesort():
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    def sort_data():
        data = wide.get()
        data = [int(x) for x in data.split()]
        bubble_sort(data)
        result_label.config(text="Sorted Data: " + ' '.join(map(str, data)))

    def clear_data():
        wide.set("")
        result_label.config(text="Sorted Data:")

    def highlight_button():
        sort_button.config(bg="light blue")  # เปลี่ยนสีพื้นหลังเป็นสีฟ้าอ่อน

    def unhighlight_button():
        sort_button.config(bg="white")  # เปลี่ยนสีพื้นหลังเป็นสีขาว

    def highlight_clear_button():
        clear_button.config(bg="light blue")  # เปลี่ยนสีพื้นหลังเป็นสีฟ้าอ่อน

    def unhighlight_clear_button():
        clear_button.config(bg="white")  # เปลี่ยนสีพื้นหลังเป็นสีขาว

    window = Toplevel()
    window.geometry("948x550")
    window.title("Bubble Sort")
    window.configure(background="grey")

    label = Label(window, text="การเรียงข้อมูลแบบฟองสบู่ (Bubble sort)", font=("Arial", 20), fg="white", bg="blue")
    label.grid(row=0, column=4, columnspan=6, padx=20, pady=20)

    label7 = Label(window, text="กรอกข้อมูล:", font=("Arial", 18), fg="black")
    label7.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

    wide = StringVar()
    txtreg1 = Entry(window, font=("Arial", 18), textvariable=wide)
    txtreg1.grid(row=1, column=5, columnspan=2)

    def generate_random_data():
        data = [random.randint(1, 100) for _ in range(5)]  # สร้างตัวเลขสุ่ม 5 ตัว (จำกัดให้มีค่าตั้งแต่ 1 ถึง 100)
        wide.set(' '.join(map(str, data)))  # กำหนดค่าข้อมูลลงในช่องข้อมูล

    random_button = Button(window, text="สุ่ม", font=("Arial", 18), fg="black", bg="white", command=generate_random_data)
    random_button.grid(row=1, column=9, padx=10, pady=10)

    label = Label(window, text="ตัวอย่าง: 6 1 8 11 9", font=("Arial", 18), fg="black")
    label.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

    sort_button = Button(window, text="จัดเรียง", font=("Arial", 18), fg="black", bg="white", command=sort_data)
    sort_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
    sort_button.bind("<Enter>", lambda event: highlight_button())  # เมื่อเมาส์ Hover เหนือปุ่ม
    sort_button.bind("<Leave>", lambda event: unhighlight_button())  # เมื่อเมาส์ออกจากปุ่ม

    result_label = Label(window, text="Sorted Data:", font=("Arial", 18), fg="black")
    result_label.grid(row=4, column=1, columnspan=6, padx=10, pady=10)

    clear_button = Button(window, text="ยกเลิก", font=("Arial", 18), fg="black", bg="white", command=clear_data)
    clear_button.grid(row=5, column=3, pady=15)
    clear_button.bind("<Enter>", lambda event: highlight_clear_button())  # เมื่อเมาส์ Hover เหนือปุ่ม "ยกเลิก"
    clear_button.bind("<Leave>", lambda event: unhighlight_clear_button())  # เมื่อเมาส์ออกจากปุ่ม "ยกเลิก"

#แบบแทรก (Insertion sort)
def Insertionsort():
    windowInsertionsort = Toplevel()
    windowInsertionsort.geometry("948x550+250+100")
    windowInsertionsort.title("Insertion sort")
    windowInsertionsort.configure(background="#FFDEAD")

    def insertionsortrandom():
        random_numbers = [random.randint(1, 100) for _ in range(4)]
        insertionspace1.delete(0, 'end')
        insertionspace1.insert(0, ' '.join(map(str, random_numbers)))

    def menuclear():
        insertionspace1.delete(0, 'end')
        insertionv.set("")
        insertionv3.set("")  # เพิ่มบรรทัดนี้เพื่อล้างช่อง "จำนวนรอบที่นับ"

    def insertion_sort(arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i
            while pos > 0 and arr[pos - 1] > cursor:
                arr[pos] = arr[pos - 1]
                pos = pos - 1
            arr[pos] = cursor
        return arr

    def insertionsortcal():
        input_numbers = insertionspace1.get()
        if not input_numbers:
            messagebox.showerror("Error", "โปรดป้อนหมายเลข")
            return
        try:
            numbers = [int(x) for x in input_numbers.split()]
        except ValueError:
            messagebox.showerror("Error", "โปรดป้อนหมายเลข และห้ามใช้ตัวอักขระ")
            return
        sorted_numbers = insertion_sort(numbers.copy())
        insertionv.set(' '.join(map(str, sorted_numbers)))
        
        # บอกจำนวนตัวเลขที่ผู้ใช้ป้อนมากี่ตัวลบ 1
        insertionv3.set(len(numbers) - 1)

    # วิตเจ็ตแต่งองค์ประกอบ    
    insertion1 = Label(windowInsertionsort, text="โปรแกรมการแทรกเรียงลำดับ", font=50, fg="black", bg="#FFDEAD")
    insertion1.place(x=350, y=20)

    label1 = Label(windowInsertionsort, text="กรอกข้อมูล", font=20, fg="white", bg="black")
    label1.place(x=200, y=80)

    label2 = Label(windowInsertionsort, text="ผลลัพธ์", font=20, fg="white", bg="black")
    label2.place(x=200, y=120)

    label3 = Label(windowInsertionsort, text="จำนวนรอบที่นับ", font=20, fg="white", bg="black")
    label3.place(x=200, y=160)

    # ช่องว่าง
    insertionv = StringVar()
    insertionv.set("")
    insertionspace1 = Entry(windowInsertionsort, font=2)
    insertionspace1.place(x=320, y=80)

    insertionspace2 = Entry(windowInsertionsort, font=2, textvariable=insertionv)
    insertionspace2.place(x=320, y=120)

    insertionv3 = StringVar()
    insertionv3.set("")
    insertionspace3 = Entry(windowInsertionsort, font=2, textvariable=insertionv3)
    insertionspace3.place(x=360, y=160)

    # ฟังก์ชันปุ่มกด
    btcal = Button(windowInsertionsort, text="คำนวณ", font=20, fg="white", bg="green", command=insertionsortcal)
    btcal.place(x=350, y=210)

    btcale = Button(windowInsertionsort, text="ยกเลิก", font=20, fg="white", bg="red", command=menuclear)
    btcale.place(x=450, y=210)

    btcale = Button(windowInsertionsort, text="สุ่มตัวเลข", font=20, fg="white", bg="#7B68EE", command=insertionsortrandom)
    btcale.place(x=390, y=260)

    windowInsertionsort.mainloop()


#แบบเลือก (Selection sort)
def Selectionsort():
    Selection = Toplevel()
    Selection.geometry("948x550+300+150")
    Selection.title("Selection Sort")
    Selection.configure(background="Light Sea Green")

    # ใส่ข้อความบรรทัดแรก
    text1 = Label(Selection,text="การเรียงลำดับข้อมูลแบบเลือก (Selection Sort)", fg="black",bg="Light Sea Green", font=("Tahoma", 13,"bold"))
    text1.grid(row=0, column=0, columnspan=5, padx=90, pady=20)

    # ข้อความ "เริ่มการเรียงข้อมูล"
    text2 = Label(Selection,text="เริ่มการเรียงข้อมูล", fg="black",bg="Light Sea Green", font=("Tahoma", 13,"bold"))
    text2.grid(row=1, column=0, columnspan=1)

    # ช่องใส่ข้อมูล
    sort3 = StringVar()
    sort3.set("")
    sort = Entry(Selection,width=30, font=5)
    sort.grid(row=1, column=1, columnspan=1)

    # ข้อความตัวอย่าง
    text3 = Label(Selection,text="ใส่ข้อมูล  ( เช่น : 5 4 9 7 30 )", fg="black", bg="Light Sea Green", font=("Tahoma", 13,"bold"))
    text3.grid(row=2, column=1, pady=3)


    # ฟังก์ชันสำหรับอัพเดตแสดงผล
    def update_display(arr, i, min_index):
        
        canvas.delete("all")
        canvas.create_text(20, 20, text="ข้อมูล:")
        canvas.create_text(80, 20, text="ขั้นตอนที่:")
        canvas.create_text(180, 20, text="ตรวจสอบ:")
        
        arrow_x = 35
        arrow_length = 5
        for idx, val in enumerate(arr):
            color = "Light Sea Green" if idx == i or idx == min_index else "black"
            canvas.create_text(20, 50 + idx * 20, text=str(val), anchor="w", fill=color)
            canvas.create_text(80, 50 + idx * 20, text=str(idx), anchor="w", fill=color)
            canvas.create_text(180, 50 + idx * 20, text="ตรวจสอบและสลับ" if idx == i else "", anchor="w", fill=color)
            
            if idx == i:
                arrow_y = 50 + idx * 20
                canvas.create_line(arrow_x, arrow_y, arrow_x + arrow_length, arrow_y - arrow_length, fill=color)
                canvas.create_line(arrow_x, arrow_y, arrow_x + arrow_length, arrow_y + arrow_length, fill=color)


    # ฟังก์ชัน Selection Sort
    def selection_sort(arr, i=0):
        
        n = len(arr)
        if i < n - 1:
            min_index = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            update_display(arr, i, min_index)
            
            step_label.config(text=f"ขั้นตอนที่ {i + 1}: {arr}")
    
            Selection.after(2000,selection_sort, arr, i + 1)
        else:
            messagebox.showinfo("สำเร็จ", "การเรียงลำดับเสร็จสิ้น")
        


    def sort_data():
        data = sort.get()  # รับข้อมูลจากช่องใส่ข้อมูล

        if not data:  
            messagebox.showerror(title="ERROR!", message="กรุณาใส่ข้อมูลก่อนครับ")
            return  

        data_list = [int(x) for x in data.split()]  # แปลงข้อมูลให้กลายเป็นรายการ
        selection_sort(data_list)

    def generate_random_data():
        data = [random.randint(1, 100) for _ in range(6)]  
        sort.delete(0, END) 
        sort.insert(0, ' '.join(map(str, data)))  
        update_display(data, -1, -1)

    def clear_data():
        sort.delete(0, END)
        step_label.config(text="")
        canvas.delete("all")
    

    # ฟังก์ชันเมื่อคลิกปุ่ม "ยืนยัน"
    button1 = Button(Selection,text="ยืนยัน", font=5, command=sort_data)
    button1.place(x=90, y=120)

    # ปุ่ม "ยกเลิก"
    button2 = Button(Selection,text="ยกเลิก", font=5, command=clear_data)
    button2.place(x=90, y=180)

    random_button = Button(Selection, text="สุ่มตัวเลข", font=5, command=generate_random_data)
    random_button.place(x=550, y=60)
    

    button1.bind("<Enter>", lambda event, btn=button1: btn.config(bg="blue"))
    button1.bind("<Leave>", lambda event, btn=button1: btn.config(bg="SystemButtonFace"))

    button2.bind("<Enter>", lambda event, btn=button2: btn.config(bg="blue"))
    button2.bind("<Leave>", lambda event, btn=button2: btn.config(bg="SystemButtonFace"))

    random_button.bind("<Enter>", lambda event, btn=random_button: btn.config(bg="GREEN"))
    random_button.bind("<Leave>", lambda event, btn=random_button: btn.config(bg="SystemButtonFace"))

    # สร้าง Canvas สำหรับแสดงผลข้อมูล
    canvas = Canvas(Selection, width=300, height=350)
    canvas.grid(row=4, column=1, pady=20)
    step_label = Label(Selection, text="", fg="black", bg="Light Sea Green", font=("Tahoma", 13,"bold"))
    step_label.grid(row=3, column=1, pady=10)

   
#แบบรวม (Merge sort)
def Mergesort():
    def randomnum():
        rand_number = []

        for _ in range(5):
            rand_num = random.randint(1,99)
            rand_number.append(rand_num)

        result = " ".join(map(str, rand_number))
    
        sort1_var.set(result)

    merge = Toplevel()
    merge.geometry("948x550+300+150")
    merge.title("Merge Sort")
    merge.configure(background="gray")

    #ใส่ข้อความบรรทัดแรก
    text1 = Label(merge,text="การเรียงลําดับข้อมูลแบบรวม (Merge Sorting)",fg="green",font=25)
    text1.grid(row=0,column=2,columnspan=5,padx=90,pady=20)

    #ข้อความ
    text2 =Label(merge,text="กรอกข้อมูล",fg="green",font=25)
    text2.grid(row=1,column=2,columnspan=1)

    #ช่องใส่ข้อมูล
    sort1_var = StringVar()
    sort1_var.set("")
    sort = Entry(merge,width=30,font=15,textvariable=sort1_var)
    sort.grid(row=1,column=3,columnspan=1)

    #ข้อความ
    text3 =Label(merge,text="ผลลัพท์",fg="green",font=25)
    text3.place(x=35,y=190)
    sort1 = Entry(merge,width=30,font=15,state="readonly")
    sort1.place(x=130,y=190)

    #ข้อความตัวอย่าง
    text3 = Label(merge,text="ตัวอย่าง : 6 1 8 11 9",fg="black",background="gray",font=10)
    text3.grid(row=2,column=3,pady=3)
            
    button1 = Button(merge,text="คำนวณ", font=3)
    button1.place(x=130,y=135) 
    button2 = Button(merge,text="ยกเลิก", font=3)
    button2.place(x=220,y=135)
    button3 = Button(merge,text="สุ่มตัวเลข", font=3,command=randomnum)
    button3.place(x=490,y=65)
 
    merge.mainloop()

#แบบลําดับ (Sequential Search)
def SequentialSearch():
    sequential = Toplevel()
    sequential.geometry("948x550")
    sequential.title("Sequential Search")
    sequential.configure(background="#C1FFC1")

    sqtitle = Label(sequential,text="Sequential Search",font=16,bg="#C1FFC1")
    sqtitle.grid(row=0,column=0,columnspan=5,padx=400,pady=20)

    sqtitle2 = Label(sequential,text="กรอกข้อมูลตัวเลข",font=20,bg="#C1FFC1")
    sqtitle2.grid(row=2,column=0,columnspan=2,padx=0,pady=20)
    sqInput = Entry(sequential,font=20)
    sqInput.grid(row=2,column=1,columnspan=2)
    sqbotton = Button(sequential,text="เพิ่ม",font=2,bg="#9BCD9B")
    sqbotton.grid(row=2,column=2,columnspan=2)

    sqtitle3 = Label(sequential,text="ค้นหาข้อมูล",font=20,bg="#C1FFC1")
    sqtitle3.grid(row=3,column=0,columnspan=2)
    sqInput2 = Entry(sequential,font=20)
    sqInput2.grid(row=3,column=1,columnspan=2)
    sqtitle4 = Label(sequential,text="ผลลัพธ์",font=20,bg="#C1FFC1")
    sqtitle4.grid(row=4,column=0,columnspan=2,padx=0,pady=20)
    sqInput3 = Entry(sequential,font=20)
    sqInput3.grid(row=4,column=1,columnspan=2)

    sqbotton2 = Button(sequential,text="ค้นหา",font=2,bg="#9BCD9B")
    sqbotton2.grid(row=5,column=1,columnspan=2,padx=0,pady=20)
    sqbotton3 = Button(sequential,text="ยกเลิก",font=2,bg="#9BCD9B")
    sqbotton3.grid(row=5,column=1,columnspan=3,padx=0,pady=20)


#แบบทวิภาค (Binary Search)
def BinarySearch():
    #สร้างหน้าต่าง Binary search
    Binary = Toplevel()
    Binary.geometry("948x550+300+150")
    Binary.title("Binary Search")
    Binary.configure(background="gray")

    #ใสข้อความบรรทัดแรก
    text1 = Label(Binary,text="การค้นหาข้อมูลแบบทวิภาค (Binary Search)",fg="green",font=25) 
    text1.grid(row=0,column=0,columnspan=5,padx=90,pady=20)

    #่ข้อความ
    text2 =Label(Binary,text="กรอกข้อมูล",fg="green",font=25)
    text2.grid(row=1,column=0,columnspan=1)

    #ช่องใส่ข้อมูล
    sort = Entry(Binary,width=30,font=15)
    sort.grid(row=1,column=1,columnspan=1)

    #ข้อความตัวอย่าง
    text3 =Label(Binary,text="ตัวอย่าง :  5 16 99 25 36",fg="black",background="gray")
    text3.grid(row=2,column=1,pady=3)

    #ปุ่มกด
    Button1 = Button(Binary,text="ยืนยัน",fg="blue",font=15)
    Button1.place(x=200,y=135)
    Button2 = Button(Binary,text="ยกเลิก",fg="gold",font=15)
    Button2.place(x=280,y=135)

#โฟลเดอร์ Sorting
def Sorting(): 
    windowsot = Toplevel(window)#หน้าต่าง sorting
    windowsot.geometry("1100x650")
    windowsot.title("Sorting")
    windowsot.iconbitmap("computer.ico")
    windowsot.configure(background="gray")

    bg = PhotoImage(file="sortfol.png")
    label1 = Label(windowsot, image=bg)
    label1.pack(expand=YES)
    
    new_image = PhotoImage(file="ai.png")
    new_button = Button(windowsot, image=new_image,width=50,height=50,command=bubblesort)  
    new_button.place(x=245,y=145)
    label1=Label(windowsot,text="Bubble Sort",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=210)

    new_image1 = PhotoImage(file="dw.png")
    new_button = Button(windowsot, image=new_image1,width=50,height=50,command=Insertionsort)  
    new_button.place(x=430,y=145)
    label1=Label(windowsot,text="Insertion Sort",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=210)

    new_image2 = PhotoImage(file="pr.png")
    new_button = Button(windowsot, image=new_image2,width=50,height=50,command=Selectionsort)  
    new_button.place(x=250,y=285)
    label1=Label(windowsot,text="Selection Sort",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=350)

    new_image3 = PhotoImage(file="xd.png")
    new_button = Button(windowsot, image=new_image3,width=50,height=50,command=Mergesort)  
    new_button.place(x=430,y=285)
    label1=Label(windowsot,text="Merge Sort",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=350)

    windowsot.mainloop()

def Searching():
    windowsrh = Toplevel(window)
    windowsrh.geometry("1100x650")
    windowsrh.title("Searching")
    windowsrh.iconbitmap("network.ico")
    windowsrh.configure(background="gray")

    bg = PhotoImage(file="sortfol.png")
    label1 = Label(windowsrh, image=bg)
    label1.pack(expand=YES)

    new_image4 = PhotoImage(file="ps.png")
    new_button = Button(windowsrh, image=new_image4,width=50,height=50,command=SequentialSearch)  
    new_button.place(x=265,y=145)
    label1=Label(windowsrh,text="Sequential Search",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=210)

    new_image5 = PhotoImage(file="au.png")
    new_button = Button(windowsrh, image=new_image5,width=50,height=50,command=BinarySearch)  
    new_button.place(x=430,y=145)
    label1=Label(windowsrh,text="Binary Search",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=210)

    windowsrh.mainloop()

image = PhotoImage(file="xplogo.png")  
button = Button(window, image=image, command=button_start, width=130, height=39)
button.place(x=1, y=700)

new_image = PhotoImage(file="thispc.png")
new_button = Button(window, image=new_image,width=50,height=50,command=Sorting)  
new_button.place(x=30,y=40)
label1=Label(window,text="Sorting",font=16,fg="white",bg="gray") 
label1.place(x=25,y=100)

Search_image1 = PhotoImage(file="network.png")
buttonU = Button(window, image=Search_image1,width=50,height=50,command=Searching)
buttonU.place(x=30,y=160)
Searchla=Label(window,text="Searching",font=16,fg="white",bg="gray") 
Searchla.place(x=15,y=225)

User_image1 = PhotoImage(file="userfolder.png")
buttonU = Button(window, image=User_image1,width=50,height=50, command=Userfol)
buttonU.place(x=30,y=270)
Userla=Label(window,text="User",font=16,fg="white",bg="gray") 
Userla.place(x=35,y=335)


window.mainloop()