from tkinter import *

window = Tk()
window.geometry("948x550+300+120")
window.title("Sorting And Searching")

bg = PhotoImage(file="winxp.png") 
label = Label(window, image=bg)
label.pack(expand=YES)

def taskbar():
    pass

image1 = PhotoImage(file="task.png")
task = Button(window, image=image1, command=taskbar, width=850, height=39)
task.place(x=135, y=503)
     
def Sorting(): 
    windowInfo = Toplevel(window) 
    windowInfo.geometry("967x542+300+120")
    windowInfo.title("Folder Sorting")
    windowInfo.configure(background="lightblue")
    bg_Sorting = PhotoImage(file="sortfol.png")
    bg_Sorting = Label(windowInfo,image=bg_Sorting)
    bg_Sorting.pack(expand=YES)

def button_start():
    winstart = Toplevel(window)
    winstart.geometry("140x120+300+505")
    pass
    
image = PhotoImage(file="xplogo.png")  
button = Button(window, image=image, command=button_start, width=130, height=39)
button.place(x=1, y=503)

new_image = PhotoImage(file="folder.png")
new_button = Button(window, image=new_image,width=50,height=50,command=Sorting)  
new_button.place(x=30,y=40)

label1=Label(window,text="Sorting",font=16,fg="white",bg="gray") 
label1.place(x=25,y=100)

window.mainloop()
