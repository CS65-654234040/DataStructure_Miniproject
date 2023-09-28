import tkinter as tk
import threading

def start_action():
    global running
    if not running:
        running = True
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        run_task()

def stop_action():
    global running
    if running:
        running = False
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

def run_task():
    if running:
        # ทำงานที่นี่
        print("กำลังทำงาน...")
        # สร้างฟังก์ชันเรียกตัวเองอีกครั้งในอนาคต
        root.after(1000, run_task)

running = False

root = tk.Tk()
root.title("Start-Stop Example")

start_button = tk.Button(root, text="Start", command=start_action)
stop_button = tk.Button(root, text="Stop", command=stop_action, state=tk.DISABLED)

start_button.pack()
stop_button.pack()

root.mainloop()
