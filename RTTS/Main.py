#! /usr/bin/python3

import paho.mqtt.client as mqtt
import urllib.request
from urllib import parse
import datetime
import time
from pymongo import MongoClient
from tkinter import *
import tkinter.font
import pickle

with open('part0.pickle', 'rb') as f:
        P= pickle.load(f)
with open('part1.pickle', 'rb') as f:
        P1= pickle.load(f)
with open('part2.pickle', 'rb') as f:
        P2= pickle.load(f)
with open('part3.pickle', 'rb') as f:
        P3= pickle.load(f)
with open('part4.pickle', 'rb') as f:
        P4= pickle.load(f)
with open('part5.pickle', 'rb') as f:
        P5= pickle.load(f)
with open('part6.pickle', 'rb') as f:
        P6= pickle.load(f)


def sendDataToServer():
    
    params = {"line_id":"001","product_id":"2","machine_id":"1","operator_id":"19","cyTime":str(Cyt),"valAddTime":str(Vat),"smvVal":"16"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)

def sendDataToServer1():
    
    params = {"line_id":"001","product_id":"2","machine_id":"2","operator_id":"20","cyTime":str(Cyt1),"valAddTime":str(Vat1),"smvVal":"96"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer2():
    
    params = {"line_id":"001","product_id":"2","machine_id":"3","operator_id":"21","cyTime":str(Cyt2),"valAddTime":str(Vat2),"smvVal":"16"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer3():
    
    params = {"line_id":"001","product_id":"2","machine_id":"4","operator_id":"31","cyTime":str(Cyt3),"valAddTime":str(Vat3),"smvVal":"28"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)

def sendDataToServer4():
    
    params = {"line_id":"001","product_id":"2","machine_id":"5","operator_id":"32","cyTime":str(Cyt4),"valAddTime":str(Vat4),"smvVal":"16"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer5():
    
    params = {"line_id":"001","product_id":"2","machine_id":"6","operator_id":"33","cyTime":str(Cyt5),"valAddTime":str(Vat5),"smvVal":"16"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer6():
    
    params = {"line_id":"001","product_id":"2","machine_id":"7","operator_id":"34","cyTime":str(Cyt6),"valAddTime":str(Vat6),"smvVal":"16"}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)




def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("Line")
    client.subscribe("Cyec")
    client.subscribe("Line1")
    client.subscribe("Cyec1")
    client.subscribe("Line2")
    client.subscribe("Cyec2")
    client.subscribe("Line3")
    client.subscribe("Cyec3")
    client.subscribe("Line4")
    client.subscribe("Cyec4")
    client.subscribe("Line5")
    client.subscribe("Cyec5")
    client.subscribe("Line6")
    client.subscribe("Cyec6")

def on_message(client, userdata, msg):
    
    receiveTime=datetime.datetime.now()
    print(msg.topic+" "+str(msg.payload))
    message=msg.payload.decode("utf-8")
    post={"time":receiveTime,"topic":msg.topic,"value":float(message)}
    print(msg.topic)
    if msg.topic == "Line":
        global Vat
        Vat = float(message)
    if msg.topic == "Cyec":
        global Cyt
        Cyt = float(message)
        global P
        P=P+1
        print("PC = "+str(P))
        with open('part0.pickle', 'wb') as f:
            pickle.dump(P, f)
            
    if msg.topic == "Line1":
        global Vat1
        Vat1 = float(message)
    if msg.topic == "Cyec1":
        global Cyt1
        Cyt1 = float(message)
        global P1
        P1=P1+1
        print("PC1 = "+str(P1))
        with open('part1.pickle', 'wb') as f:
            pickle.dump(P1, f)
            
    if msg.topic == "Line2":
        global Vat2
        Vat2 = float(message)
    if msg.topic == "Cyec2":
        global Cyt2
        Cyt2 = float(message)
        global P2
        P2=P2+1
        print("PC2 = "+str(P2))
        with open('part2.pickle', 'wb') as f:
            pickle.dump(P2, f)
            
    if msg.topic == "Line3":
        global Vat3
        Vat3 = float(message)
    if msg.topic == "Cyec3":
        global Cyt3
        Cyt3 = float(message)
        global P3
        P3=P3+1
        print("PC3 = "+str(P3))
        with open('part3.pickle', 'wb') as f:
            pickle.dump(P3, f)
            
    if msg.topic == "Line4":
        global Vat4
        Vat4 = float(message)
    if msg.topic == "Cyec4":
        global Cyt4
        Cyt4 = float(message)
        global P4
        P4=P4+1
        print("PC4 = "+str(P4))
        with open('part4.pickle', 'wb') as f:
            pickle.dump(P4, f)
            
    if msg.topic == "Line5":
        global Vat5
        Vat5 = float(message)
    if msg.topic == "Cyec5":
        global Cyt5
        Cyt5 = float(message)
        global P5
        P5=P5+1
        print("PC5 = "+str(P5))
        with open('part5.pickle', 'wb') as f:
            pickle.dump(P5, f)
            
    if msg.topic == "Line6":
        global Vat6
        Vat6 = float(message)
    if msg.topic == "Cyec6":
        global Cyt6
        Cyt6 = float(message)
        global P6
        P6=P6+1
        print("PC6 = "+str(P6))
        with open('part6.pickle', 'wb') as f:
            pickle.dump(P6, f)
        
    collection.insert_one(post)
        
# Set up client for MongoDB
mongoClient=MongoClient()
db=mongoClient.SensorData
collection=db.line_data
    
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.55", 1883, 60)
client.loop_start()

# initialise variable to starting value
Vat = 0
Cyt = 0
PrevCyt = 0
D = 0
Vat1 = 0
Cyt1 = 0
PrevCyt1 = 0
D1 = 0
Vat2 = 0
Cyt2 = 0
PrevCyt2 = 0
D2 = 0
Vat3 = 0
Cyt3 = 0
PrevCyt3 = 0
D3 = 0
Vat4 = 0
Cyt4 = 0
PrevCyt4 = 0
D4 = 0
Vat5 = 0
Cyt5 = 0
PrevCyt5 = 0
D5 = 0
Vat6 = 0
Cyt6 = 0
PrevCyt6 = 0
D6 = 0

while True:
    if PrevCyt != Cyt:
        sendDataToServer()
        D=D+1
        print("SDC = "+str(D))
    PrevCyt=Cyt
    if PrevCyt1 != Cyt1: #and Cyt1 <= 150:
        sendDataToServer1()
        D1=D1+1
        print("SDC1 = "+str(D1))
    PrevCyt1=Cyt1
    if PrevCyt2 != Cyt2:# and Cyt2 <= 40:
        sendDataToServer2()
        D2=D2+1
        print("SDC2 = "+str(D2))
    PrevCyt2=Cyt2
    if PrevCyt3 != Cyt3:# and Cyt3 <= 60:
        sendDataToServer3()
        D3=D3+1
        print("SDC3 = "+str(D3))
    PrevCyt3=Cyt3
    if PrevCyt4 != Cyt4:# and Cyt <= 50:
        sendDataToServer4()
        D4=D4+1
        print("SDC4 = "+str(D4))
    PrevCyt4=Cyt4
    if PrevCyt5 != Cyt5:
        sendDataToServer5()
        D5=D5+1
        print("SDC5 = "+str(D5))
    PrevCyt5=Cyt5
    if PrevCyt6 != Cyt6:# and Cyt6 <= 50:
        sendDataToServer6()
        D6=D6+1
        print("SDC6 = "+str(D6))
    PrevCyt6=Cyt6
    

