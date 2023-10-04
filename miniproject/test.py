import tkinter as tk

# สร้างหน้าต่างหลัก
root = tk.Tk()

# สร้างฟังก์ชันสำหรับเปิดหน้าต่างย่อย
def open_window():
    new_window = tk.Toplevel(root)
    new_window.title("หน้าต่างย่อย")
    tk.Label(new_window, text="นี่คือหน้าต่างย่อย").pack()
    tk.Button(new_window, text="ปิดหน้าต่างนี้", command=new_window.destroy).pack()

# สร้างปุ่มเพื่อเปิดหน้าต่างย่อย
tk.Button(root, text="เปิดหน้าต่างย่อย", command=open_window).pack()

# สร้างปุ่มเพื่อเคลียร์หน้าต่างทั้งหมด
def clear_windows():
    # หากต้องการเคลียร์หน้าต่างย่อยก็สามารถใช้คำสั่งนี้
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.destroy()

tk.Button(root, text="เคลียร์หน้าต่างทั้งหมด", command=clear_windows).pack()

# เริ่มการทำงานของ tkinter
root.mainloop()
