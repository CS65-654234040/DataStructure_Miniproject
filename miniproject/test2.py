import tkinter as tk
from tkinter import messagebox

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

window = tk.Tk()
window.geometry("948x550")
window.title("Bubble Sort")
window.configure(background="grey")

label = tk.Label(window, text="การเรียงข้อมูลแบบฟองสบู่ (Bubble sort)", font=("Arial", 20), fg="white", bg="blue")
label.grid(row=0, column=4, columnspan=6, padx=20, pady=20)

label7 = tk.Label(window, text="กรอกข้อมูล:", font=("Arial", 18), fg="black")
label7.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

wide = tk.StringVar()
txtreg1 = tk.Entry(window, font=("Arial", 18), textvariable=wide)
txtreg1.grid(row=1, column=5, columnspan=2)

label = tk.Label(window, text="ตัวอย่าง: 6 1 8 11 9", font=("Arial", 18), fg="black")
label.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

sort_button = tk.Button(window, text="จัดเรียง", font=("Arial", 18), fg="black", bg="white", command=sort_data)
sort_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)
sort_button.bind("<Enter>", lambda event: highlight_button())  # เมื่อเมาส์ Hover เหนือปุ่ม
sort_button.bind("<Leave>", lambda event: unhighlight_button())  # เมื่อเมาส์ออกจากปุ่ม

result_label = tk.Label(window, text="Sorted Data:", font=("Arial", 18), fg="black")
result_label.grid(row=4, column=1, columnspan=6, padx=10, pady=10)

clear_button = tk.Button(window, text="ยกเลิก", font=("Arial", 18), fg="black", bg="white", command=clear_data)
clear_button.grid(row=5, column=3, pady=15)
clear_button.bind("<Enter>", lambda event: highlight_clear_button())  # เมื่อเมาส์ Hover เหนือปุ่ม "ยกเลิก"
clear_button.bind("<Leave>", lambda event: unhighlight_clear_button())  # เมื่อเมาส์ออกจากปุ่ม "ยกเลิก"

window.mainloop()