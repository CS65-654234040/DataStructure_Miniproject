from tkinter import *

# Function to create new windows
def User():
    #แบ้ง
    window1 = Toplevel(window)
    window1.title("หน้าต่างใหม่")
    window1.geometry("350x360+150+200")
    window1.configure(bg="#006CFF")

    img1 = PhotoImage(file="040.png")
    label1 = Label(window1,bg="#006CFF",image=img1)
    label1.pack()
    text1 = Label(window1,text="ผู้จัดทำ", font=("Tahoma", 13,"bold"))
    text1.pack(expand=YES)
    text2 = Label(window1,text="User : อนุศิษฎ์ ปานพิมเสน\nPassword : 654234040\nหน้าที่ : Merge Sort", font=("Tahoma", 13,"bold"),background="#006CFF",fg="white")
    text2.pack(expand=YES)

    #นัง
    window2 = Toplevel(window)
    window2.title("หน้าต่างใหม่")
    window2.geometry("350x360+550+200")
    
    img2 = PhotoImage(file="solo.png")
    label2 = Label(window2, image=img2)
    label2.pack()

    #พี
    window3 = Toplevel(window)
    window3.title("หน้าต่างใหม่")
    window3.geometry("350x360+950+200")
    
    img3 = PhotoImage(file="499.png")
    label3 = Label(window3, image=img3)
    label3.pack()

    #อัง
    window4 = Toplevel(window)
    window4.title("หน้าต่างใหม่")
    window4.geometry("350x360+150+600")
    
    img4 = PhotoImage(file="499.png")
    label4 = Label(window4, image=img4)
    label4.pack()

    #อานัส
    window5 = Toplevel(window)
    window5.title("หน้าต่างใหม่")
    window5.geometry("350x360+550+600")
    
    img5 = PhotoImage(file="499.png")
    label5 = Label(window5, image=img5)
    label5.pack()

    #ต้น
    window6 = Toplevel(window)
    window6.title("หน้าต่างใหม่")
    window6.geometry("350x360+950+600")
    
    img6 = PhotoImage(file="499.png")
    label6 = Label(window6, image=img6)
    label6.pack()
    img7 = PhotoImage(file="png")
    label7 = Label(window, image=img7)
    label7.pack()


# Function to close the main window
def close_window():
    window.destroy()

window = Tk()
window.geometry("300x300+150+120")
window.title("หน้าต่างหลัก")

button_create = Button(window, text="สร้างหน้าต่างใหม่", command=User)
button_create.pack()

button_quit = Button(window, text="ปิดหน้าต่างหลัก", command=close_window)
button_quit.pack()

window.mainloop()