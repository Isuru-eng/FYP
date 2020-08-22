#! /usr/bin/python3

import time
from time import localtime, strftime
import pickle
import os

file = open("/home/pi/RTTS/hourley.csv", "a")
i=0
if os.stat("/home/pi/RTTS/hourley.csv").st_size == 0:
    file.write("Time,St_1,St_2,St_3,St_4,St_5,St_6,St_7\n")


def save_counter():
    with open('part0.pickle', 'rb') as f:
            global R
            R = pickle.load(f)
    time.sleep(5)
    with open('part1.pickle', 'rb') as f:
            global R1
            R1= pickle.load(f)
    time.sleep(5)
    with open('part2.pickle', 'rb') as f:
            global R2
            R2= pickle.load(f)
    time.sleep(5)
    with open('part3.pickle', 'rb') as f:
            global R3
            R3= pickle.load(f)
    time.sleep(5)
    with open('part4.pickle', 'rb') as f:
            global R4
            R4= pickle.load(f)
    time.sleep(5)
    with open('part5.pickle', 'rb') as f:
            global R5
            R5= pickle.load(f)
    time.sleep(5)
    with open('part6.pickle', 'rb') as f:
            global R6
            R6= pickle.load(f)
    time.sleep(5)
    file.write(str(time.strftime("%H", localtime()))+","+str(R)+","+str(R1)+","+str(R2)+","+str(R3)+","+str(R4)+","+str(R5)+","+str(R6)+"\n")
    file.flush()

def reset_counter():
    with open('part0.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part1.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part2.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part3.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part4.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part5.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    with open('part6.pickle', 'wb') as f:
            pickle.dump(0, f)
    time.sleep(5)
    
while True:
    time_now = time.strftime("%M", localtime())
    time.sleep(30)
    print(time_now)
    
    if time_now == "00":
        print("Saving")
        save_counter()
        time.sleep(15)
        print("Resetting")
        reset_counter()
        file.write(str(localtime())+","+str(R)+","+str(R1)+","+str(R2)+","+str(R3)+","+str(R4)+","+str(R5)+","+str(R6)+"\n")
        file.flush()
        file.close()
