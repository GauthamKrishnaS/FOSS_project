
from tkinter import *
import platform

root = Tk()

root.title("System Information")
root.geometry("470x320")
root.configure(bg="#2d363b")

quit_button = Button(root, text ="Exit", command=root.quit,padx=10, pady=5, fg="#ffffff", bg="#ed3418", font="helvetica")

label_1 = Label(root,text="Kernel & System info \n ____________________________" ,fg="white",bg="#2d363b", font="helvetica")
OS = Label(root , text="Operting System : "+ platform.system() , padx=10, pady=5, fg="white",bg="#2d363b",anchor = CENTER, font="helvetica")
Platform = Label(root , text="Platform : "+ platform.platform() , padx=10, pady=5, fg="white",bg="#2d363b",anchor = CENTER, font="helvetica")
Node = Label(root, text="Node :"+ platform.node(), padx=10, pady=5, fg="white",bg="#2d363b",anchor = CENTER, font="helvetica")
Release = Label(root, text="Operating system release number : "+ platform.release(), padx=10, pady=5,fg="white", bg="#2d363b",anchor = CENTER, font="helvetica")
KernelVersion = Label(root, text="Kernel Version : "+ platform.version(),  padx=10, pady=5, fg="white",bg="#2d363b",anchor = CENTER, font="helvetica")
Machine = Label(root, text="Hardware type : "+ platform.machine(), padx=10, pady=5, fg="white",bg="#2d363b",anchor = CENTER, font="helvetica")

label_1.pack()
OS.pack()
KernelVersion.pack()
Platform.pack()
Node.pack()
Release.pack()
Machine.pack()
quit_button.pack()

root.mainloop()
