from tkinter import *

def show_user_info():
    window1 = Toplevel(window)
    window1.title("หน้าต่างใหม่")
    window1.geometry("350x360+150+200")
    window1.configure(bg="#006CFF")

    img1 = PhotoImage(file="040.png")
    label1 = Label(window1, bg="#006CFF", image=img1)
    label1.pack()
    text1 = Label(window1, text="ผู้จัดทำ", font=("Tahoma", 13, "bold"))
    text1.pack(expand=YES)
    text2 = Label(
        window1,
        text="User : อนุศิษฎ์ ปานพิมเสน\nPassword : 654234040\nหน้าที่ : Merge Sort",
        font=("Tahoma", 13, "bold"),
        background="#006CFF",
        fg="white",
    )
    text2.pack(expand=YES)

def show_nang():
    window2 = Toplevel(window)
    window2.title("หน้าต่างใหม่")
    window2.geometry("350x360+550+200")

    img2 = PhotoImage(file="solo.png")
    label2 = Label(window2, image=img2)
    label2.pack()

def show_phee():
    window3 = Toplevel(window)
    window3.title("หน้าต่างใหม่")
    window3.geometry("350x360+950+200")

    img3 = PhotoImage(file="499.png")
    label3 = Label(window3, image=img3)
    label3.pack()

def show_ang():
    window4 = Toplevel(window)
    window4.title("หน้าต่างใหม่")
    window4.geometry("350x360+150+600")

    img4 = PhotoImage(file="499.png")
    label4 = Label(window4, image=img4)
    label4.pack()

def show_aunnas():
    window5 = Toplevel(window)
    window5.title("หน้าต่างใหม่")
    window5.geometry("350x360+550+600")

    img5 = PhotoImage(file="499.png")
    label5 = Label(window5, image=img5)
    label5.pack()

def show_ton():
    window6 = Toplevel(window)
    window6.title("หน้าต่างใหม่")
    window6.geometry("350x360+950+600")

    img6 = PhotoImage(file="499.png")
    label6 = Label(window6, image=img6)
    label6.pack()

window = Tk()
window.title("Main Window")
window.geometry("800x600")


btn_user = Button(window, text="แบ้ง", command=show_user_info)
btn_user.pack(side=LEFT)

btn_nang = Button(window, text="นัง", command=show_nang)
btn_nang.pack(side=LEFT)

btn_phee = Button(window, text="พี", command=show_phee)
btn_phee.pack(side=LEFT)

btn_ang = Button(window, text="อัง", command=show_ang)
btn_ang.pack(side=LEFT)

btn_aunnas = Button(window, text="อานัส", command=show_aunnas)
btn_aunnas.pack(side=LEFT)

btn_ton = Button(window, text="ต้น", command=show_ton)
btn_ton.pack(side=LEFT)

window.mainloop()
