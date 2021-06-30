#===============================START==================================

from tkinter import *
from tkinter import messagebox

#================================Functions================================

def clear():
    global optr
    optr=""
    s1.set("")
    s2.set(0)

def btnclick(num):
    global optr
    optr=optr + str(num)
    s1.set(optr)

def ans():
    global optr
    a=str(eval(optr))
    s2.set(a)

#================================Window================================

root=Tk()
root.title("CALCULATOR")
root.geometry("350x400")
root.configure(bg="white")

s1=StringVar()
s1.set("")
s2=StringVar()
s2.set("")
optr=""

#================================Entry Box==================================

e1=Entry(root, font=("Arial", 12, "bold"), textvariable=s1, bg="pink", bd=10, insertwidth=2, justify="right")
e1.place(x=25, y=20, width=305, height=45)
e2=Entry(root, font=("Arial", 12, "bold"), textvariable=s2, bg="pink", bd=10, insertwidth=2, justify="right")
e2.place(x=25, y=80, width=305, height=45)

#=================================Buttons====================================

#================================Numbers==============================

b1=Button(root, text="1", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(1))
b1.place(x=30, y=140)
b2=Button(root, text="2", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(2))
b2.place(x=90, y=140)
b3=Button(root, text="3", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(3))
b3.place(x=150, y=140)

b4=Button(root, text="4", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(4))
b4.place(x=30, y=200)
b5=Button(root, text="5", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(5))
b5.place(x=90, y=200)
b6=Button(root, text="6", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(6))
b6.place(x=150, y=200)

b7=Button(root, text="7", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(7))
b7.place(x=30, y=260)
b8=Button(root, text="8", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(8))
b8.place(x=90, y=260)
b9=Button(root, text="9", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(9))
b9.place(x=150, y=260)
b0=Button(root, text="0", bg="cyan", fg="red", bd=8, width=5, height=2, command=lambda: btnclick(0))
b0.place(x=90, y=320)

#=============================Operators================================

bA=Button(root, text="+", bg="yellow", fg="red", bd=8, width=5, height=6, command=lambda: btnclick("+"))
bA.place(x=210, y=140)
bS=Button(root, text="_", bg="yellow", fg="red", bd=8, width=5, height=2, command=lambda: btnclick("-"))
bS.place(x=210, y=260)
bM=Button(root, text="*", bg="yellow", fg="red", bd=8, width=5, height=2, command=lambda: btnclick("*"))
bM.place(x=270, y=140)
bD=Button(root, text="/", bg="yellow", fg="red", bd=8, width=5, height=2, command=lambda: btnclick("/"))
bD.place(x=270, y=200)
bP=Button(root, text="%", bg="yellow", fg="red", bd=8, width=5, height=2, command=lambda: btnclick("%"))
bP.place(x=270, y=260)

#===========================Command Buttons==================================

b10=Button(root, text="ANS", bg="green", fg="white", bd=8, width=12, height=2, command=ans)
b10.place(x=215, y=320)
b11=Button(root, text="CLEAR", bg="orange", bd=8, width=5, height=2, command=clear)
b11.place(x=30, y=320)
b12=Button(root, text="EXIT", bg="red", fg="white", bd=8, width=5, height=2, command=root.destroy)
b12.place(x=150, y=320)

#============================END===========================================

root.mainloop()
