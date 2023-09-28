from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#สร้างหน้าต่างเมนูหลัก
window = Tk()
window.geometry("1500x745")
window.title("Sorting And Searching")

#พื้นหลังหน้าจอหลัก
bg = PhotoImage(file="winxp.png") 
label = Label(window, image=bg)
label.pack(expand=YES)

#taskbar
image1 = PhotoImage(file="task.png")
task = Button(window, image=image1,  width=1500, height=39)
task.place(x=135, y=700)
     
#ฟังชั่นในปุ่ม window     
def button_start():
    pass

#แบบฟองสบู่ (Bubble sort)
def bubblesort():
    window = Toplevel()
    window.geometry("948x550")
    window.title("Bubble Sort")
    window.configure(background="grey")

    def menuExit():
        window.destroy()

    label = Label(window, text="การเรียงข้อมูลแบบฟองสบู่ (Bubble sort)", font=("Arial", 20), fg="white", bg="blue")
    label.grid(row=0, column=2, columnspan=5, padx=125, pady=20)

    label7 = Label(window, text="กรอกข้อมูล", font=("Arial", 18), fg="black", bg="white")
    label7.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

    wide = StringVar()
    txtreg1 = Entry(window, font=("Arial", 18), textvariable=wide)
    txtreg1.grid(row=1, column=4, columnspan=2)

    label = Label(window, text=" ตัวอย่าง : 6 1 8 11 9 ", font=("Arial", 20), fg="black")
    label.grid(row=2,column=4,columnspan=2,padx=10,pady=10)

#แบบแทรก (Insertion sort)
def Insertionsort():
    windowInsertionsort = Tk()
    windowInsertionsort.geometry("948x550+250+100")
    windowInsertionsort.title("Insertion sort")
    windowInsertionsort.configure(background="gray")

    def menuclear():
        insertionspace1.delete(0, 'end')  # ล้างข้อมูลใน Entry widget
        insertionv.set("")  # ล้างข้อมูลใน StringVar
    # สร้างฟังก์ชัน Insertion Sort
    def insertion_sort(arr, simulation=False):

        for i in range(len(arr)):
            cursor = arr[i]
            pos = i

            while pos > 0 and arr[pos - 1 ] > cursor:
            #สลับเลขภายในลิสต์
                arr[pos] = arr[pos - 1 ]
                pos = pos - 1
            arr[pos] = cursor

        return arr
    # ฟังก์ชันคำนวณ Insertion Sort
    def insertionsortcal():
        data = insertionspace1.get()
        try:
            # แปลงข้อมูลจากข้อความเป็นรายการตัวเลข
            data_list = list(map(int, data.split()))
            # เรียงลำดับข้อมูลด้วย Insertion Sort
            insertion_sort(data_list)
            # แสดงผลลัพธ์ที่เรียงลำดับแล้วใน insertionspace2
            result = " ".join(map(str, data_list))
            insertionv.set(result)
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ถูกต้อง")

    insertion1 = Label(windowInsertionsort,text="โปรแกรมการแทรกเรียงลำดับ", font=50, fg="white", bg="Blue")
    insertion1.place( x=350, y=20)

    label1 = Label(windowInsertionsort,text="กรอกข้อมูล", font=20, fg="white", bg="black")
    label1.place(x=200, y=80)

    label1 = Label(windowInsertionsort,text="ผลลัพธ์", font=20, fg="white", bg="black")
    label1.place(x=200, y=120)

    insertionv = StringVar()
    insertionv.set("")
    insertionspace1 = Entry(windowInsertionsort,font=2)
    insertionspace1.place(x=320, y=80)

    insertionspace2 = Entry(windowInsertionsort,font=2, textvariable=insertionv)  
    insertionspace2.place(x=320, y=120)

    btcal = Button(windowInsertionsort, text="คำนวณ", font=20, fg="white", bg="green", command=insertionsortcal)
    btcal.place(x=350, y=180)

    btcale = Button(windowInsertionsort, text="ยกเลิก",font=20,fg="white",bg="red",command=menuclear)
    btcale.place(x=450, y=180)


#แบบเลือก (Selection sort)
def Selectionsort():
    # สร้างหน้าต่าง Selection Sort
    Selection = Toplevel()
    Selection.geometry("948x550+300+150")
    Selection.title("Selection Sort")
    Selection.configure(background="gray")

    # ใส่ข้อความบรรทัดแรก
    text1 = Label(Selection,text="การเรียงลำดับข้อมูลแบบเลือก (Selection Sort)", fg="green", font="25")
    text1.grid(row=0, column=0, columnspan=5, padx=90, pady=20)

    # ข้อความ "เริ่มการเรียงข้อมูล"
    text2 = Label(Selection,text="เริ่มการเรียงข้อมูล", fg="green", font=25)
    text2.grid(row=1, column=0, columnspan=1)

    # ช่องใส่ข้อมูล
    sort = Entry(Selection,width=30, font=5)
    sort.grid(row=1, column=1, columnspan=1)

    # ข้อความตัวอย่าง
    text3 = Label(Selection,text="ตัวอย่าง :  5 4 9 7 1", fg="black", bg="gray", font=5)
    text3.grid(row=2, column=1, pady=3)

    # ฟังก์ชันสำหรับอัพเดตแสดงผล
    def update_display(arr, i, min_index):
        canvas.delete("all")  # ล้างการแสดงผล
        canvas.create_text(20, 20, text="ข้อมูล:")
        canvas.create_text(80, 20, text="ขั้นตอนที่:")
        canvas.create_text(180, 20, text="เลือก:")
        for idx, val in enumerate(arr):
            color = "blue" if idx == i or idx == min_index else "black"
            canvas.create_text(20, 50 + idx * 20, text=str(val), anchor="w", fill=color)
            canvas.create_text(80, 50 + idx * 20, text=str(idx), anchor="w", fill=color)
            canvas.create_text(180, 50 + idx * 20, text="เลือก" if idx == i else "", anchor="w", fill=color)

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
            Selection.after(100, selection_sort, arr, i + 1)
    def sort_data():
        data = sort.get()  # รับข้อมูลจากช่องใส่ข้อมูล
        data_list = [int(x) for x in data.split()]  # แปลงข้อมูลให้กลายเป็นรายการ
        selection_sort(data_list)

    # ฟังก์ชันเมื่อคลิกปุ่ม "ยืนยัน"
    def sort_data():
        data = sort.get()  # รับข้อมูลจากช่องใส่ข้อมูล
        data_list = [int(x) for x in data.split()]  # แปลงข้อมูลให้กลายเป็นรายการ
        selection_sort(data_list)  # เรียงข้อมูลด้วย Selection Sort

    # ปุ่ม "ยืนยัน"
    button1 = Button(Selection,text="ยืนยัน", font=5, command=sort_data)
    button1.place(x=90, y=120)

    # ปุ่ม "ยกเลิก"
    button2 = Button(Selection,text="ยกเลิก", font=5, command=Selection.quit)
    button2.place(x=90, y=180)

    # สร้าง Canvas สำหรับแสดงผลข้อมูล
    canvas = Canvas(Selection, width=300, height=350)
    canvas.grid(row=4, column=1, pady=20)

#แบบรวม (Merge sort)
def Mergesort():
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
    sort = Entry(merge,width=30,font=15)
    sort.grid(row=1,column=3,columnspan=1)

    #ข้อความตัวอย่าง
    text3 = Label(merge,text="ตัวอย่าง : 6 1 8 11 9",fg="black",background="gray",font=10)
    text3.grid(row=2,column=3,pady=3)

    button1 = Button(merge,text="ยืนยัน", font=3)
    button1.place(x=190,y=135) 
    button2 = Button(merge,text="ยกเลิก", font=3)
    button2.place(x=280,y=135)

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
    windowsot.configure(background="gray")

    bg = PhotoImage(file="sortfol.png")
    label1 = Label(windowsot, image=bg)
    label1.pack(expand=YES)
    
    new_image = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image,width=50,height=50,command=bubblesort)  
    new_button.place(x=245,y=145)
    label1=Label(windowsot,text="Bubble Sort",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=210)

    new_image1 = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image1,width=50,height=50,command=Insertionsort)  
    new_button.place(x=430,y=145)
    label1=Label(windowsot,text="Insertion Sort",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=210)

    new_image2 = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image2,width=50,height=50,command=Selectionsort)  
    new_button.place(x=250,y=285)
    label1=Label(windowsot,text="Selection Sort",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=350)

    new_image3 = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image3,width=50,height=50,command=Mergesort)  
    new_button.place(x=430,y=285)
    label1=Label(windowsot,text="Merge Sort",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=350)

    new_image4 = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image4,width=50,height=50,command=SequentialSearch)  
    new_button.place(x=250,y=400)
    label1=Label(windowsot,text="Sequential Search",font=13,fg="white",bg="gray") 
    label1.place(x=220,y=470)

    new_image5 = PhotoImage(file="folder.png")
    new_button = Button(windowsot, image=new_image5,width=50,height=50,command=BinarySearch)  
    new_button.place(x=430,y=400)
    label1=Label(windowsot,text="Binary Search",font=13,fg="white",bg="gray") 
    label1.place(x=400,y=470)

    windowsot.mainloop()

image = PhotoImage(file="xplogo.png")  
button = Button(window, image=image, command=button_start, width=130, height=39)
button.place(x=1, y=700)

new_image = PhotoImage(file="folder.png")
new_button = Button(window, image=new_image,width=50,height=50,command=Sorting)  
new_button.place(x=30,y=40)

label1=Label(window,text="Sorting",font=16,fg="white",bg="gray") 
label1.place(x=25,y=100)

window.mainloop()