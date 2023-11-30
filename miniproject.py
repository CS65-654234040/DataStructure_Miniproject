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
    window.destroy()
    pass


#แบบฟองสบู่ (Bubble sort)
def bubblesort():
    bubblesort = Toplevel()
    bubblesort.geometry("948x550+250+100")
    bubblesort.title("Bubble Sort")
    bubblesort.configure(background="lightgreen")

    # ฟังก์ชันยกเลิก
    def cancel():
        sort.delete(0, END)
        sort1.delete(0, END)

    # ใส่ข้อความบรรทัดแรก
    text1 = Label(bubblesort, text="การเรียงลําดับข้อมูลแบบฟองสบู่", fg="green", font=25)
    text1.place(x=320, y=80)
    text2 = Label(bubblesort, text="กรอกข้อมูล", fg="green", font=25)
    text2.place(x=160, y=140)
    text3 = Label(bubblesort, text="ผลลัพธ์", fg="green", font=25)
    text3.place(x=160, y=190)

    # ช่องใส่ข้อมูล
    sort1_var = StringVar()
    sort1_var.set("")
    sort = Entry(bubblesort, width=30, font=15, textvariable=sort1_var)
    sort.place(x=260, y=140)

    # เพิ่มช่องสำหรับแสดงผลลัพธ์
    sort1 = Entry(bubblesort, width=30, font=15)
    sort1.place(x=260, y=190)

    # ข้อความตัวอย่าง
    text3 = Label(bubblesort, text="ตัวอย่าง: 6 1 8 11 9", fg="black", background="gray", font=10)
    text3.place(x=320, y=280)

    # ฟังก์ชันสุ่มตัวเลข
    def buble_random_numbers():
        random_numbers = " ".join(str(random.randint(1, 100)) for _ in range(5))
        sort.delete(0, END)
        sort.insert(0, random_numbers)

    # ฟังก์ชัน Bubble Sort
    def bubble_sort(input_list, reverse=False):
        n = len(input_list)
        for i in range(n):
            for j in range(0, n - i - 1):
                if (not reverse and input_list[j] > input_list[j + 1]) or (reverse and input_list[j] < input_list[j + 1]):
                    input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]

    # ฟังก์ชันทำการเรียงข้อมูล
    def bubble_cal():
        input_list = list(map(int, sort.get().split()))
        reverse = sorting_order.get() == 2  # 2 คือมากไปน้อย
        bubble_sort(input_list, reverse)
        sorted_numbers = " ".join(map(str, input_list))
        sort1.delete(0, END)
        sort1.insert(0, sorted_numbers)

    # ปุ่มคำนวณ
    button1 = Button(bubblesort, text="คำนวณ", font=3,bg="blue",fg="white", command=bubble_cal)
    button1.place(x=280, y=340)

    button2 = Button(bubblesort, text="ยกเลิก", font=3,bg="blue",fg="white", command=cancel)
    button2.place(x=420, y=340)

    # ปุ่มสุ่มตัวเลข
    button3 = Button(bubblesort, text="สุ่มตัวเลข", font=3,bg="blue",fg="white", command=buble_random_numbers)
    button3.place(x=650, y=160)

    # เพิ่มตัวแปรสำหรับเลือกการเรียงลำดับ
    sorting_order = IntVar()
    sorting_order.set(1)  # 1 คือเรียงมากไปน้อย

    max_to_min_button = Radiobutton(bubblesort, text="น้อยไปมาก", variable=sorting_order, value=1)
    max_to_min_button.place(x=330, y=240)

    min_to_max_button = Radiobutton(bubblesort, text="มากไปน้อย", variable=sorting_order, value=2)
    min_to_max_button.place(x=430, y=240)

    bubblesort.mainloop()

#แบบแทรก (Insertion sort)
def Insertionsort():
    windowInsertionsort = Toplevel()
    windowInsertionsort.geometry("750x400+250+100")
    windowInsertionsort.title("Insertion sort")
    windowInsertionsort.configure(background="#FFDEAD")
    #ฟังชันก์สุ่มตัวเลข
    def insertionsortrandom():
        random_numbers = [random.randint(1, 100) for _ in range(4)]
        insertionspace1.delete(0, END)
        insertionspace1.insert(0, ' '.join(map(str, random_numbers)))
    #เมนูเคลียร์
    def menuclear():
        insertionspace1.delete(0, END)
        insertionv.set("")
        insertionv3.set("")
    #กรณีจากมากไปน้อย
    def insertion_sort_maxmin(arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i - 1
            while pos >= 0 and cursor > arr[pos]:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            arr[pos + 1] = cursor
        return arr
    #กรณีจากน้อยไปมาก
    def insertion_sort_minmax(arr):
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i - 1
            while pos >= 0 and cursor < arr[pos]:
                arr[pos + 1] = arr[pos]
                pos = pos - 1
            arr[pos + 1] = cursor
        return arr
    #กรณีโชว์เออเร่อ
    def insertionsorterror():
        input_numbers = insertionspace1.get()
        if not input_numbers:
            messagebox.showerror(title="Information", message="โปรดป้อนหมายเลข")
            return
        try:
            numbers = [int(x) for x in input_numbers.split()]
        except ValueError:
            messagebox.showerror(title="Error", message="โปรดป้อนหมายเลข และห้ามใช้ตัวอักขระ")
            return
        if radiovar.get() == 1:
            sorted_numbers = insertion_sort_minmax(numbers.copy())
        elif radiovar.get() == 2:
            sorted_numbers = insertion_sort_maxmin(numbers.copy())
        else:
            messagebox.showerror(title="Error", message="โปรดเลือกวิธีการเรียงลำดับ")
            return
        insertionv.set(' '.join(map(str, sorted_numbers)))
        insertionv3.set(len(numbers) - 1)
    #หัวข้อ
    insertion1 = Label(windowInsertionsort, text="โปรแกรมการแทรกเรียงลำดับ", font=50, fg="black", bg="#FFDEAD")
    insertion1.place(x=350, y=20)
    #บรรทัดกรอกข้อมูล
    insertionv = StringVar()
    insertionv.set("")
    insertionspace1 = Entry(windowInsertionsort, font=2)
    insertionspace1.place(x=320, y=80)
    label1 = Label(windowInsertionsort, text="กรอกข้อมูล", font=20, fg="white", bg="black")
    label1.place(x=200, y=80)
    #บรรทัดผลลัพธ์
    insertionspace2 = Entry(windowInsertionsort, font=2, textvariable=insertionv)
    insertionspace2.place(x=320, y=120)
    label2 = Label(windowInsertionsort, text="ผลลัพธ์", font=20, fg="white", bg="black")
    label2.place(x=200, y=120)
    #บรรทัดจำนวนที่นับ
    insertionv3 = StringVar()
    insertionv3.set("")
    insertionspace3 = Entry(windowInsertionsort, font=2, textvariable=insertionv3)
    insertionspace3.place(x=360, y=160)
    label3 = Label(windowInsertionsort, text="จำนวนรอบที่นับ", font=20, fg="white", bg="black")
    label3.place(x=200, y=160)
    #ปุ่ม
    btcal = Button(windowInsertionsort, text="คำนวณ", font=20, fg="white", bg="green", command=insertionsorterror)
    btcal.place(x=350, y=290)

    btcale = Button(windowInsertionsort, text="ยกเลิก", font=20, fg="white", bg="red", command=menuclear)
    btcale.place(x=450, y=290)

    btcale = Button(windowInsertionsort, text="สุ่มตัวเลข", font=20, fg="white", bg="#0000FF", command=insertionsortrandom)
    btcale.place(x=570, y=75)

    radiovar = IntVar()
    radiovar.set(0)
    min_max = Radiobutton(windowInsertionsort, text="จำนวนน้อยไปมาก",font=15,fg="black",bg="#FFDEAD",variable=radiovar,value=1)
    min_max.place(x=350, y=200)
    max_min = Radiobutton(windowInsertionsort, text="จำนวนมากไปน้อย",font=15,fg="black",bg="#FFDEAD",variable=radiovar,value=2)
    max_min.place(x=350, y=250)

    windowInsertionsort.mainloop()

#แบบเลือก (Selection sort)
def Selectionsort():
    windowselectionsort = Toplevel()
    windowselectionsort.geometry("700x300+250+100")
    windowselectionsort.title("Selection sort")
    windowselectionsort.configure(background="#FFDEAD")
    
    #เมนูสำหรับเคลียร์
    def menuclear():
        selectionspace1.delete(0, END)
        selectionv.set("")
        selectionv3.set("")
    
    #เมนูสำหรับการสุ่ม
    def windowselectionsortrandom():
        random_numbers = [random.randint(1, 100) for _ in range(4)]
        selectionspace1.delete(0, END)
        selectionspace1.insert(0, ' '.join(map(str, random_numbers)))
    
    #เมนูสำหรับการเก็บค่ามากไปน้อย
    def selectionerror():
        input_list = list(map(int,selectionspace1.get().split()))
        reverse = True if calculation_option.get() == "มากไปน้อย" else False
        selection_sort(input_list, reverse)
        sorted_numbers = " ".join(map(str, input_list))
        selectionv.set(sorted_numbers)
    #นี้คือสูตร
    def selection_sort(arr,reverse=False):
        for i in range(len(arr)): #สร้าง for i สำหรับ โดยไห้ rang ทำตามจำนวนของ len ที่นับ arr
            min_idx = i #สร้างตัวแปรสำหรับ index
            for j in range(i+1, len(arr)):#สร้างfor j สำหรับเช็คค่า โดยไห้ rang ทำตามจำนวนของ i+1 และสิ้นสุดที่ rang ทำตามจำนวนของ len ที่นับ arr
                if arr[j] < arr[min_idx] if reverse else arr[j] > arr[min_idx] :#เช็คว่าถ้า arr ใน index ของ j น้อยกว่า arr ใน min idex ถูกต้องหรือไม่ ถ้าเข้าเงื่อนไข จะเข้าบรรทัดถัดไป
                    min_idx = j#สั่งไห้ min index = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]#หลังจากทำใน rang เสร็จแล้ว จะสลับค่า arr i ไปที่ arr min index และ arr min index สลับไปที่ arr i
        return arr#ส่งออกค่าในตัวแปร arr

    def selectionerror():
        input_numbers = selectionspace1.get()
        if not input_numbers:
            messagebox.showerror("Error", "โปรดป้อนหมายเลข")
            return
        try:
            numbers = [int(x) for x in input_numbers.split()]
        except ValueError:
            messagebox.showerror("Error", "โปรดป้อนหมายเลข และห้ามใช้ตัวอักขระ")
            return
        #รับค่าน้อยไปมาก
        reverse = calculation_option.get() == "น้อยไปมาก"
        sorted_numbers = selection_sort(numbers.copy(), reverse)
        
        selectionv.set(' '.join(map(str, sorted_numbers)))
        selectionv3.set(len(numbers) - 1)
    selection1 = Label(windowselectionsort, text="โปรแกรมการเรียงลำดับด้วยวิธีการเลือก", font=("Tahoma", 13,"bold"), fg="black", bg="#FFDEAD")
    selection1.place(x=250, y=20)
    #สร้างเมนูกรอกข้อมูล
    label1 = Label(windowselectionsort, text="กรอกข้อมูล", font=("Tahoma", 13,"bold"), fg="white", bg="black")
    label1.place(x=120, y=80)
    #สร้างเมนูผลลัพธ์
    label2 = Label(windowselectionsort, text="ผลลัพธ์",font=("Tahoma", 13,"bold"), fg="white", bg="black")
    label2.place(x=150, y=200)
   
    #สร้างเมนูEntry
    selectionv = StringVar()
    selectionv.set("")
    selectionspace1 = Entry(windowselectionsort, font=10)
    selectionspace1.place(x=220, y=80)
    selectionv3 = StringVar()
    
    selectionv3.set("")
    selectionspace2 = Entry(windowselectionsort, font=10, textvariable=selectionv)
    selectionspace2.place(x=250, y=200)
    
    # เพิ่ม OptionMenu สำหรับเลือกรูปแบบการคำนวณ
    calculation_option = StringVar()
    calculation_option.set("มากไปน้อย")  # ตัวเลือกเริ่มต้น
    option_menu = OptionMenu(windowselectionsort, calculation_option,"มากไปน้อย", "น้อยไปมาก")
    option_menu.configure(font=("Tahoma", 13,"bold"),fg="black",bg="gray",width=10,height=1)
    option_menu.place(x=350, y=135)
    
    #สร้างเมนูคำนวณ
    btcal = Button(windowselectionsort, text="คำนวณ", font=("Tahoma", 13,"bold"), fg="white", bg="green", command=selectionerror)
    btcal.place(x=250, y=135)
    #สร้างเมนูเคลียร์
    btcale = Button(windowselectionsort, text="เคลียร์", font=("Tahoma", 13,"bold"), fg="white", bg="red", command=menuclear)
    btcale.place(x=550, y=135)
    #สร้างเมนูสุ่มตัวเลข
    btcale = Button(windowselectionsort, text="สุ่มตัวเลข",font=("Tahoma", 13,"bold"), fg="white", bg="#0000FF", command=windowselectionsortrandom)
    btcale.place(x=470, y=75)

#แบบรวม (Merge sort)
def Mergesort():
    mergesort = Toplevel()
    mergesort.geometry("700x300+250+100")
    mergesort.title("Merge Sort")
    mergesort.configure(background="gray")

    def merge_sort(arr, reverse=False): #ฟังชั่น merge_sort รับค่า arr และค่า reverse ,arr = รับมาจาก def merge_cal() ,
        #โดยใน def จะเรียกใช้ merge_sortโดยส่งค่าinput_list และ reverse ไป 
        if len(arr) > 1: #ให้เช็คโดยนับค่าของ arr ว่ามีกี่ตัว โดย len จะทำการนับ จำนวน index เริ่มจาก 1 ,ซึ่งถ้าตัวที่เช็ค > 1 เข้าเงื่อนไขแรก
            mid = len(arr) // 2 #ให้ตัวแปรใหม่ mid เก็บ จำนวน index หาร 2  
            left_half = arr[:mid] #สร้างตัวแปรเก็บค่า ซ้าย --> left ให้ left เริ่มที่ตัวแรกของอาเรย์ไปจนถึง ค่า mid
            right_half = arr[mid:] #สร้างตัวแปรเก็บค่า ขวา --> right ให้ right เริ่มที่ ค่า mid ไปจนถึงค่าสุดท้ายของอาเรย์

            merge_sort(left_half, reverse)  #เรียกฟังชั่นซ้ำ เพื่อส่งค่า left_half ที่หาได้
            merge_sort(right_half, reverse) #เรียกฟังชั่นซ้ำ เพื่อส่งค่า right_half ที่หาได้

            i = 0 #กำหนดให้ค่า i  คือ 0 (เก็บค่า L)
            j = 0 #กำหนดให้ค่า j  คือ 0 (เก็บค่า R)
            k = 0 #กำหนดให้ค่า k  คือ 0 (เก็บค่า index ของ arr)

            while i < len(left_half) and j < len(right_half): #เป็นการสร้างลูป while โดยถ้า i > indexของleft_half และ j < index ของ right_half
                if (left_half[i] > right_half[j]) if reverse else (left_half[i] < right_half[j]): 
                    # เปรียบเทียบค่า left_half[i] กับ right_half[j] ซึ่งขึ้นอยู่กับค่าของ reverse 
                    # ***กรณี (left_half[i] > right_half[j])
                    arr[k] = left_half[i] #ให้ left_half ที่ index i ไปแทนใน ตำแหน่งที่ k ของ arr 
                    i += 1 #ให้ i = i + 1
                else: # ***กรณี (left_half[i] < right_half[j])
                    arr[k] = right_half[j] #ให้ right_half ที่ index j ไปไปแทนใน ตำแหน่งที่ k ของ arr
                    j += 1 #ให้ j = j + 1
                k += 1 #เมื่อทำใน if,else เสร็จแล้ว จะให้ k = k + 1 
            # เมื่อทำครบแล้วให้เอาค่าที่ได้ทั้งหมด ไปเช็ค while อีกครั้งจนกว่าจะไม่เข้าใน while แล้วจึง while ถัดไป
            while i < len(left_half): #เช็คว่า i < ความยาวของ left_half หรือไม่
                arr[k] = left_half[i] #ให้ left_half ที่ index i ไปแทนในตำแหน่งที่ k ของ arr 
                i += 1 # ให้ i = i + 1
                k += 1 # ให้ k = k + 1

            while j < len(right_half): #เช็คว่า j < ความยาวของ right_half หรือไม่
                arr[k] = right_half[j] #ให้ right_half ที่ index j ไปแทนในตำแหน่งที่ k ของ arr
                j += 1 # ให้ j = j + 1
                k += 1 # ให้ k = k + 1

    def merge_cal(): #สร้างฟังชั่น คำนวณ
        input_list = list(map(int, enter.get().split())) #สร้าตัวแปร ให้ค่า คือสิ่งที่รับมา
        # enter.get() --> รับข้อมูลจากที่ผู้ใช้ป้อน
        # split() --> แบ่งข้อความที่ได้จาก enter.get() เป็นส่วนๆ โดยให้ " " (space)  เช่น "7,1,3" เป็น ["7", "1", "3"]
        # map(int, ...)แปลงทุกสตริงในรายการที่ได้จาก split() ให้กลายเป็นตัวเลข (integer) โดยใช้ฟังชั่น int ในการแปลง เช่น ["7", "1", "3"]-->[7, 1, 3]
        # list(...) ใช้ในการแปลงผลลัพธ์จาก map ให้กลายเป็นรายการของตัวเลข โดยดูจาก input_list-->[7, 1, 3]
        reverse = True if calculation_option.get() == "มากไปน้อย" else False #เก็บค่า True , False
        # reverse จะ = True เมื่อ ผู้ใช้เลือก "มากไปน้อย"
        # reverse จะ = False เมื่อ ผู้ใช้เลือกตัวเลือกอื่น --> "น้อยไปมาก"
        merge_sort(input_list, reverse) #เรียกใช้ merge_sort โดยส่งค่า input_list และ reverse ไป
        sorted_numbers = " ".join(map(str, input_list)) #สร้างตัวแปรให้ ตัวแปร = map(str, input_list) คือ ทุกตัวใน input_list = สตริง ," ".join คือ เอา สตริงทุกตัวมารวมกันโดยให้ " " แบ่งระหว่างและผลลัพ จะทำกับ สตริงเดี่ยว
        enterStrSet.set(sorted_numbers) #enterStrSet จะเก็บค่าเพื่อให้แสดงในโค้ดหลักช่องผลลัพท์ โดย set คือจะให้ ผลลัพท์คือ sorted_numbers

    def cleardata():
        enter.delete(0, END)
        enterStrSet.set("")

    def random_number():
        random_numbers = " ".join(str(random.randint(1, 100)) for _ in range(9))
        enter.delete(0, END)
        enter.insert(0, random_numbers)

    head = Label(mergesort,font=("Tahoma", 13,"bold"), text="การเรียงลําดับข้อมูลแบบรวม (Merge Sorting)", fg="green")
    head.grid(row=0, column=2, columnspan=5, padx=90, pady=20)

    text_inputnum = Label(mergesort,font=("Tahoma", 13,"bold"), text="กรอกข้อมูล", fg="green")
    text_inputnum.grid(row=1, column=2, columnspan=1)

    #ช่องใส่เลขที่จะเพิ่ม
    enterStrSet = StringVar()
    enterStrSet.set("")
    enter = Entry(mergesort, width=30, font=15, textvariable=enterStrSet)
    enter.grid(row=1, column=3, columnspan=1)

    text_result = Label(mergesort,font=("Tahoma", 13,"bold"), text="ผลลัพท์", fg="green")
    text_result.place(x=35, y=190)

    enterStrSet = StringVar()
    enterStrSet.set("")
    sort1_entry = Entry(mergesort, width=30, font=15, textvariable=enterStrSet, state='readonly')
    sort1_entry.place(x=130, y=190)

    textEx = Label(mergesort,font=("Tahoma", 13,"bold"), text="ตัวอย่าง : 6 1 8 11 9", fg="black", background="gray")
    textEx.grid(row=2, column=3, pady=3)

    # เพิ่ม OptionMenu สำหรับเลือกรูปแบบการคำนวณ
    calculation_option = StringVar()
    calculation_option.set("น้อยไปมาก")  # ตัวเลือกเริ่มต้น
    option_menu = OptionMenu(mergesort, calculation_option, "น้อยไปมาก", "มากไปน้อย")
    option_menu.configure(font=("Tahoma", 13,"bold"),fg="white",bg="gray",width=10,height=1)
    option_menu.place(x=230, y=135)

    buttonCal = Button(mergesort,font=("Tahoma", 13,"bold"), text="คำนวณ", command=merge_cal, bg="blue", fg="white")
    buttonCal.place(x=135, y=135)

    buttonclear = Button(mergesort,font=("Tahoma", 13,"bold"), text="เคลียร์", command=cleardata, bg="red", fg="white")
    buttonclear.place(x=450, y=135)

    buttonrandomnum = Button(mergesort,font=("Tahoma", 13,"bold"), text="สุ่มตัวเลข", command=random_number, bg="green", fg="white")
    buttonrandomnum.place(x=490, y=65)

    mergesort.mainloop()

#แบบลําดับ (Sequential Search)
def SequentialSearch():
    sequential = Toplevel()
    sequential.geometry("948x550")
    sequential.title("Sequential Search")
    sequential.configure(background="#C1FFC1")


    def exit ():
        sequential.destroy()

    def clear ():
        cal.set(" ")
        cal2.set(" ")
        cal3.set(" ")

    def reset_array():
        data1.clear()  # Clear the list
        lb.delete(0, END)  # Clear the listbox

    data1 = []

    def add_number():
        input_text = cal.get()
        if input_text.strip():  # Check if the input is not empty
            input_numbers = input_text.split()  # Split input by whitespace
            for num_str in input_numbers:
                try:
                    number = int(num_str)
                    data1.append(number)
                    lb.insert(END, number)
                except ValueError:
                    # Handle non-integer input
                    pass
            cal.set("")  # Clear the input field

    def search():
        target = int(cal2.get())
        position = -1
        for i, num in enumerate(data1):
            if num == target:
                position = i
                break
        sqInput3.config(state="normal")
        if position != -1:
            sqInput3.delete(0, END)
            sqInput3.insert(0, f"พบข้อมูล {target} ที่ตำแหน่ง {position}")
        else:
            sqInput3.delete(0, END)
            sqInput3.insert(0, "ไม่พบข้อมูลที่ต้องการค้นหา")
        sqInput3.config(state="readonly")

    sqtitle = Label(sequential,text="Sequential Search",font=16,bg="#C1FFC1")
    sqtitle.grid(row=0,column=0,columnspan=5,padx=400,pady=20)

    cal = StringVar()
    cal.set(" ")
    sqtitle2 = Label(sequential,text="กรอกข้อมูลตัวเลข",font=20,bg="#C1FFC1")
    sqtitle2.grid(row=2,column=0,columnspan=2,padx=0,pady=20)
    sqInput = Entry(sequential,font=20,textvariable=cal)
    sqInput.grid(row=2,column=1,columnspan=2)


    sqbotton = Button(sequential,text="เพิ่ม",font=2,bg="#9BCD9B",command=add_number)
    sqbotton.grid(row=2,column=2,columnspan=2)


    sqbotton4 = Button(sequential,text="Reset",font=2,bg="#9BCD9B",command=reset_array)
    sqbotton4.grid(row=3,column=2,columnspan=2)

    cal2 = StringVar()
    cal2.set(" ")
    sqtitle3 = Label(sequential,text="ค้นหาข้อมูล",font=20,bg="#C1FFC1")
    sqtitle3.grid(row=3,column=0,columnspan=2)
    sqInput2 = Entry(sequential,font=20,textvariable=cal2)
    sqInput2.grid(row=3,column=1,columnspan=2)


    cal3 = StringVar()
    cal.set(" ")
    sqtitle4 = Label(sequential,text="ผลลัพธ์",font=20,bg="#C1FFC1")
    sqtitle4.grid(row=4,column=0,columnspan=2,padx=0,pady=20)
    sqInput3 = Entry(sequential,font=20,textvariable=cal3)
    sqInput3["state"] = "readonly"
    sqInput3.grid(row=4,column=1,columnspan=2)

    sqbotton2 = Button(sequential,text="ค้นหา",font=2,bg="#9BCD9B",command=search)
    sqbotton2.grid(row=5,column=1,columnspan=2,padx=0,pady=20)

    sqbotton3 = Button(sequential,text="ยกเลิก",font=2,bg="#9BCD9B",command=clear)
    sqbotton3.grid(row=5,column=1,columnspan=3,padx=0,pady=20)

    sqbotton5 = Button(sequential,text="Exit",font=2,bg="#9BCD9B",command=exit)
    sqbotton5.grid(row=5,column=2,columnspan=4,padx=0,pady=20)

    lb = Listbox(sequential, font=("Arial", 20))
    lb.grid(row=6, column=0, columnspan=4, padx=20, pady=20)

    sequential.mainloop()

#แบบทวิภาค (Binary Search)
def BinarySearch():
    my_array = []

    def add_number():
        input_text = entry_add.get()
        if input_text.strip():
            input_numbers = input_text.split()
            for num_str in input_numbers:
                try:
                    number = int(num_str)
                    my_array.append(number)
                    lb.insert(END, number)
                except ValueError:
                    pass

    def binsearch(t):
        L = 0
        R = len(my_array) - 1
        while L <= R:
            M = (L + R) // 2
            if my_array[M] == t:
                return True, M, my_array[M]
            elif my_array[M] > t:
                R = M - 1
            elif my_array[M] < t:
                L = M + 1
        return False, None, None

    def search_button_clicked():
        search_values = entry_search.get().split()
        results = []
        for value in search_values:
            try:
                search_value = int(value)
                result, index, value = binsearch(search_value)
                if result:
                    results.append(f"พบที่ดัชนี {index}: {value}")
                else:
                    results.append(f"ไม่พบค่า {search_value}")
            except ValueError:
                results.append(f"ไม่ถูกต้อง: {value}")
        result_label.config(text='\n'.join(results))

    def generate_random_numbers():
        random_numbers = ' '.join(str(random.randint(1, 100)) for _ in range(5))
        entry_add.delete(0, "end")
        entry_add.insert(0, random_numbers)

    def sort_array():
        my_array.sort()
        baimai.delete(0, "end")  # Clear the Entry widget
        baimai.insert(0, ' '.join(map(str, my_array)))  # Insert the sorted values

    # Create the main tkinter window
    binary = Toplevel()
    binary.geometry("650x550+250+100")
    binary.title("การค้นหาแบบทวิภาค")
    binary.configure(background="pink")
    text1 = Label(binary,text="การค้นหาข้อมูลแบบทวิภาค (Binary Search)", fg="GREEN", font=25)
    text1.place(x=100,y=10)

    # Create and layout GUI elements
    label_add = Label(binary, text="ป้อนค่าที่ต้องการเพิม:",font=("Tahoma",12))
    label_add.place(x=10, y=80)
    entry_add = Entry(binary,font=("Tahoma",15))
    entry_add.place(x=180, y=80)

    label_search = Label(binary, text="ป้อนค่าที่ต้องการค้นหา:",font=("Tahoma",12))
    label_search.place(x=10, y=160)

    label_sort = Label(binary, text="เรียงลำดับ:",font=("Tahoma",12))
    label_sort.place(x=10, y=120)

    baimai = Entry(binary,font=("Tahoma",15))
    baimai.place(x=180, y=120)

    entry_search = Entry(binary,font=("Tahoma", 15))
    entry_search.place(x=180, y=160)

    search_button = Button(binary, text="ค้นหา",font=("Tahoma",12), command=search_button_clicked)
    search_button.place(x=420, y=160)

    add_button = Button(binary, text="เพิม",font=("Tahoma",12) ,command=add_number)
    add_button.place(x=420, y=80)

    sort_button = Button(binary, text="เรียงลำดับ",font=("Tahoma",12), command=sort_array)
    sort_button.place(x=420, y=120)

    result_label = Label(binary, text="คำตอบ", font=("Arial", 15))
    result_label.place(x=10, y=200)

    # "สุ่มตัวเลข" button
    random_button = Button(binary,text="สุ่มตัวเลข", font=15, command=generate_random_numbers, bg="white")
    random_button.place(x=200, y=240)

    def clear_fields():
        entry_add.delete(0, "end")  # เคลียข้อมูลใน entry_add
        entry_search.delete(0, "end")  # เคลียข้อมูลใน entry_search
        result_label.config(text="")  # ลบข้อความใน result_label
        baimai.delete(0,"end")
        my_array.clear()  # Clear the list
        lb.delete(0, END)  # Clear the listbox

    clear_button = Button(binary, text="Clear", command=clear_fields, font=15)
    clear_button.place(x=400, y=240)

    lb = Listbox(binary, font=("Arial", 20))
    lb.place(x=100,y=300)

    binary.mainloop()


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

#โฟลเดอร์ Sorting
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