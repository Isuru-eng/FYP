#! /usr/bin/python3

import tkinter as tk
import pickle
from tkinter import *
import tkinter.font

master = tk.Tk()
lbl = Label(master, text="0", font=("Arial Bold", 20))
lbl.grid(column=1, row=0)
lblL = Label(master, text="Station 1 = ", font=("Arial Bold", 20))
lblL.grid(column=0, row=0)
lble = Label(master, text="SMV", font=("Arial Bold", 20))
lble.grid(column=2, row=0)
e = Entry(master)
e.grid(column=3, row=0)
btn=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input())
btn.grid(column=4, row=0)



lbl1 = Label(master, text="0", font=("Arial Bold", 20))
lbl1.grid(column=1, row=1)
lbl1L = Label(master, text="Station 2 = ", font=("Arial Bold", 20))
lbl1L.grid(column=0, row=1)
lble1 = Label(master, text="SMV", font=("Arial Bold", 20))
lble1.grid(column=2, row=1)
e1 = Entry(master)
e1.grid(column=3, row=1)
btn1=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input1())
btn1.grid(column=4, row=1)

lbl2 = Label(master, text="0", font=("Arial Bold", 20))
lbl2.grid(column=1, row=2)
lbl2L = Label(master, bg ="red", text="Station 3 = ", font=("Arial Bold", 20))
lbl2L.grid(column=0, row=2)
lble2 = Label(master, text="SMV", font=("Arial Bold", 20))
lble2.grid(column=2, row=2)
e2 = Entry(master)
e2.grid(column=3, row=2)
btn2=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input2())
btn2.grid(column=4, row=2)

lbl3 = Label(master, text="0", font=("Arial Bold", 20))
lbl3.grid(column=1, row=3)
lbl3L = Label(master, bg ="red", text="Station 4 = ", font=("Arial Bold", 20))
lbl3L.grid(column=0, row=3)
lble3 = Label(master, text="SMV", font=("Arial Bold", 20))
lble3.grid(column=2, row=3)
e3 = Entry(master)
e3.grid(column=3, row=3)
btn3=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input3())
btn3.grid(column=4, row=3)

lbl4 = Label(master, text="0", font=("Arial Bold", 20))
lbl4.grid(column=1, row=4)
lbl4L = Label(master, bg ="red", text="Station 5 = ", font=("Arial Bold", 20))
lbl4L.grid(column=0, row=4)
lble4 = Label(master, text="SMV", font=("Arial Bold", 20))
lble4.grid(column=2, row=4)
e4 = Entry(master)
e4.grid(column=3, row=4)
btn4=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input4())
btn4.grid(column=4, row=4)

lbl5 = Label(master, text="0", font=("Arial Bold", 20))
lbl5.grid(column=1, row=5)
lbl5L = Label(master, bg ="red", text="Station 6 = ", font=("Arial Bold", 20))
lbl5L.grid(column=0, row=5)
lble5 = Label(master, text="SMV", font=("Arial Bold", 20))
lble5.grid(column=2, row=5)
e5 = Entry(master)
e5.grid(column=3, row=5)
btn5=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input5())
btn5.grid(column=4, row=5)

lbl6 = Label(master, text="0", font=("Arial Bold", 20))
lbl6.grid(column=1, row=6)
lbl6L = Label(master, text="Station 7 = ", font=("Arial Bold", 20))
lbl6L.grid(column=0, row=6)
lble6 = Label(master, text="SMV", font=("Arial Bold", 20))
lble6.grid(column=2, row=6)
e6 = Entry(master)
e6.grid(column=3, row=6)
btn6=Button(master, height=1, width=10, text="Commit",command=lambda: retrieve_input6())
btn6.grid(column=4, row=6)


def retrieve_input():
    global SMV
    SMV=e.get()
    with open('SMV.pickle', 'wb') as f:
        pickle.dump(SMV, f)

def retrieve_input1():
    global SMV1
    SMV1=e1.get()
    with open('SMV1.pickle', 'wb') as f:
        pickle.dump(SMV1, f)

def retrieve_input2():
    global SMV2
    SMV2=e2.get()
    with open('SMV2.pickle', 'wb') as f:
        pickle.dump(SMV2, f)

def retrieve_input3():
    global SMV3
    SMV3=e3.get()
    with open('SMV3.pickle', 'wb') as f:
        pickle.dump(SMV3, f)

def retrieve_input4():
    global SMV4
    SMV4=e4.get()
    with open('SMV4.pickle', 'wb') as f:
        pickle.dump(SMV4, f)

def retrieve_input5():
    global SMV5
    SMV5=e5.get()
    with open('SMV5.pickle', 'wb') as f:
        pickle.dump(SMV5, f)

def retrieve_input6():
    global SMV6
    SMV6=e6.get()
    with open('SMV6.pickle', 'wb') as f:
        pickle.dump(SMV6, f)        

def my_mainloop():
    with open('part0.pickle', 'rb') as f:
        P1= pickle.load(f)
    #print(P1)
    lbl.config(text=str(P1))

    with open('part1.pickle', 'rb') as f:
        P2= pickle.load(f)
    #print(P2)
    lbl1.config(text=str(P2))

    with open('part2.pickle', 'rb') as f:
        P3= pickle.load(f)
    #print(P3)
    lbl2.config(text=str(P3))

    with open('part3.pickle', 'rb') as f:
        P4= pickle.load(f)
    #print(P4)
    lbl3.config(text=str(P4))

    with open('part4.pickle', 'rb') as f:
        P5= pickle.load(f)
    #print(P5)
    lbl4.config(text=str(P5))

    with open('part5.pickle', 'rb') as f:
        P6= pickle.load(f)
    #print(P6)
    lbl5.config(text=str(P6))

    with open('part6.pickle', 'rb') as f:
        P7= pickle.load(f)
    #print(P7)
    lbl6.config(text=str(P7))

    master.after(1000, my_mainloop)

master.after(1000, my_mainloop)

master.mainloop()
