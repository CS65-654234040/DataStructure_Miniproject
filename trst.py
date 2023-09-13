import tkinter as tk

def start_menu_click():
    start_menu.post(start_button.winfo_rootx(), start_button.winfo_rooty() + start_button.winfo_height())

def ปิด():  
    root.destroy()

root = tk.Tk()
root.title("ปุ่ม Start แบบ Windows XP")

# สร้างปุ่ม "Start"
start_button = tk.Button(root, text="Start", width=10, height=2, command=start_menu_click)
start_button.pack(pady=10)

# สร้างเมนูย่อย "Start"
start_menu = tk.Menu(root, tearoff=0)
start_menu.add_command(label="โปรแกรม")
start_menu.add_command(label="เอกสาร")
start_menu.add_separator()
start_menu.add_command(label="ปิด",command=ปิด)

# เพิ่มไอคอน (รูปภาพ "Start" ของ Windows XP)
#start_image = tk.PhotoImage(file="")  # แทน "start.png" ด้วยตำแหน่งไฟล์ภาพของคุณ
#start_button.config(image=start_image, compound=tk.LEFT)
start_button.config(compound=tk.LEFT)
#start_button.image = start_image  # จำเป็นต้องเก็บอ้างอิงไอคอนเพื่อประสิทธิภาพ

# กำหนดเมนูย่อยให้กับปุ่ม "Start"
#start_button.config(menu=start_menu)

root.mainloop()