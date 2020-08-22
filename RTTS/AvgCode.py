#! /usr/bin/python3

import paho.mqtt.client as mqtt
import urllib.request
from urllib import parse
import datetime
import time
from time import gmtime, strftime
from pymongo import MongoClient
from tkinter import *
import tkinter.font
import pickle
import os

#variable store

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
        
#time n array
        
#time_now = strftime("%M", gmtime())
readingsv = []
readingsc = []

#time_now1 = strftime("%M", gmtime())
readingsv1 = []
readingsc1 = []

#time_now2 = strftime("%M", gmtime())
readingsv2 = []
readingsc2 = []

#time_now3 = strftime("%M", gmtime())
readingsv3 = []
readingsc3 = []

#time_now4 = strftime("%M", gmtime())
readingsv4 = []
readingsc4 = []

#time_now5 = strftime("%M", gmtime())
readingsv5 = []
readingsc5 = []

#time_now6 = strftime("%M", gmtime())
readingsv6 = []
readingsc6 = []

#CSV
file = open("/home/pi/RTTS/data_log.csv", "a")
i=0
if os.stat("/home/pi/RTTS/data_log.csv").st_size == 0:
    file.write("Module,Time,Vat,Cyt\n")


def sendDataToServer():

    with open('SMV.pickle', 'rb') as f:
        global smv
        smv= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"1","operator_id":"19","cyTime":str(avgCyt),"valAddTime":str(avgVat),"smvVal":str(smv)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)

def sendDataToServer1():

    with open('SMV1.pickle', 'rb') as f:
        global smv1
        smv1= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"2","operator_id":"20","cyTime":str(avgCyt1),"valAddTime":str(avgVat1),"smvVal":str(smv1)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer2():

    with open('SMV2.pickle', 'rb') as f:
        global smv2
        smv2= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"3","operator_id":"21","cyTime":str(avgCyt2),"valAddTime":str(avgVat2),"smvVal":str(smv2)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer3():

    with open('SMV3.pickle', 'rb') as f:
        global smv3
        smv3= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"4","operator_id":"31","cyTime":str(avgCyt3),"valAddTime":str(avgVat3),"smvVal":str(smv3)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)

def sendDataToServer4():

    with open('SMV4.pickle', 'rb') as f:
        global smv4
        smv4= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"5","operator_id":"32","cyTime":str(avgCyt4),"valAddTime":str(avgVat4),"smvVal":str(smv4)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
    
def sendDataToServer5():

    with open('SMV5.pickle', 'rb') as f:
        global smv5
        smv5= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"6","operator_id":"33","cyTime":str(avgCyt5),"valAddTime":str(avgVat5),"smvVal":str(smv5)}
    querystring = parse.urlencode(params)
    print(querystring)
    url = "https://realtimevisualization.000webhostapp.com/sql/insertData_cycleTime.php"+"?"+querystring
    resp = urllib.request.urlopen(url)
        
def sendDataToServer6():

    with open('SMV6.pickle', 'rb') as f:
        global smv6
        smv6= pickle.load(f)
    
    params = {"line_id":"001","product_id":"2","machine_id":"7","operator_id":"34","cyTime":str(avgCyt6),"valAddTime":str(avgVat6),"smvVal":str(smv6)}
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
#---------------------------------------------------------------------------------
    if msg.topic == "Line":
        global Vat
        Vat = float(message)
#avg data
        global readingsv
        global max_samplesv
        readingv = Vat
        #max_samplesv = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv.append(readingv)
        global avgVat
        avgVat = mean(readingsv)
        
    if msg.topic == "Cyec":
        global Cyt
        Cyt = float(message)
#part count        
        global P
        P=P+1
        print("PC = "+str(P))
        with open('part0.pickle', 'wb') as f:
            pickle.dump(P, f)
        file.write(str(1)+","+str(receiveTime)+","+str(Vat)+","+str(Cyt)+"\n")
        file.flush()
#avg data
        global readingsc
        global max_samplesc
        readingc = Cyt
        max_samplesc = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc.append(readingc)
        global avgCyt
        avgCyt = mean(readingsc)
        print(avgCyt)
#send data        
        if len(readingsc) >= max_samplesc: #or strftime("%M", gmtime()) >= time_now+10:
            print("data sending0")
            sendDataToServer()
            readingsc = []
            readingsv = []
            #avgCyt = 0
            #time_now = strftime("%M", gmtime())

#------------------------------------------------------------------------------

    if msg.topic == "Line1":
        global Vat1
        Vat1 = float(message)
#avg data
        global readingsv1
        global max_samplesv1
        readingv1 = Vat
        #max_samplesv1 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv1.append(readingv1)
        global avgVat1
        avgVat1 = mean(readingsv1)
        
    if msg.topic == "Cyec1":
        global Cyt1
        Cyt1 = float(message)
#part count        
        global P1
        P1=P1+1
        print("PC1 = "+str(P1))
        with open('part1.pickle', 'wb') as f:
            pickle.dump(P1, f)
        file.write(str(2)+","+str(receiveTime)+","+str(Vat1)+","+str(Cyt1)+"\n")
        file.flush()
#avg data
        global readingsc1
        global max_samplesc1
        readingc1 = Cyt
        max_samplesc1 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc1.append(readingc1)
        global avgCyt1
        avgCyt1 = mean(readingsc1)
        print(avgCyt1)
#send data        
        if len(readingsc1) >= max_samplesc1: #or strftime("%M", gmtime()) >= time_now1+10:
            print("data sending1")
            sendDataToServer1()
            readingsc1 = []
            readingsv1 = []
            #avgCyt1 = 0
            #time_now1 = strftime("%M", gmtime())

#------------------------------------------------------------------------------

    if msg.topic == "Line2":
        global Vat2
        Vat2 = float(message)
#avg data
        global readingsv2
        #global max_samplesv2
        readingv2 = Vat2
        max_samplesv2 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv2.append(readingv2)
        global avgVat2
        avgVat2 = mean(readingsv2)
        
    if msg.topic == "Cyec2":
        global Cyt2
        Cyt2 = float(message)
#part count        
        global P2
        P2=P2+1
        print("PC2 = "+str(P2))
        with open('part2.pickle', 'wb') as f:
            pickle.dump(P2, f)
        file.write(str(3)+","+str(receiveTime)+","+str(Vat2)+","+str(Cyt2)+"\n")
        file.flush()
#avg data
        global readingsc2
        global max_samplesc2
        readingc2 = Cyt2
        max_samplesc2 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc2.append(readingc2)
        global avgCyt2
        avgCyt2 = mean(readingsc2)
        print(avgCyt2)
#send data        
        if len(readingsc2) >= max_samplesc2: # or strftime("%M", gmtime()) >= time_now2+10:
            print("data sending2")
            sendDataToServer2()
            readingsc2 = []
            readingsv2 = []
            #avgCyt2 = 0
            #time_now2 = strftime("%M", gmtime())

#------------------------------------------------------------------------------

    if msg.topic == "Line3":
        global Vat3
        Vat3 = float(message)
#avg data
        global readingsv3
        #global max_samplesv3
        readingv3 = Vat3
        max_samplesv3 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv3.append(readingv3)
        global avgVat3
        avgVat3 = mean(readingsv3)
        
    if msg.topic == "Cyec3":
        global Cyt3
        Cyt3 = float(message)
#part count        
        global P3
        P3=P3+1
        print("PC3 = "+str(P3))
        with open('part3.pickle', 'wb') as f:
            pickle.dump(P3, f)
        file.write(str(4)+","+str(receiveTime)+","+str(Vat3)+","+str(Cyt3)+"\n")
        file.flush()
#avg data
        global readingsc3
        global max_samplesc3
        readingc3 = Cyt3
        max_samplesc3 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc3.append(readingc3)
        global avgCyt3
        avgCyt3 = mean(readingsc3)
        print(avgCyt3)
#send data        
        if len(readingsc3) >= max_samplesc3: # or strftime("%M", gmtime()) >= time_now3+10:
            print("data sending3")
            sendDataToServer3()
            readingsc3 = []
            readingsv3 = []
            #avgCyt3 = 0
            #time_now3 = strftime("%M", gmtime())

#------------------------------------------------------------------------------

    if msg.topic == "Line4":
        global Vat4
        Vat4 = float(message)
#avg data
        global readingsv4
        #global max_samplesv4
        readingv4 = Vat4
        max_samplesv4 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv4.append(readingv4)
        global avgVat4
        avgVat4 = mean(readingsv4)
        
    if msg.topic == "Cyec4":
        global Cyt4
        Cyt4 = float(message)
#part count        
        global P4
        P4=P4+1
        print("PC4 = "+str(P4))
        with open('part4.pickle', 'wb') as f:
            pickle.dump(P4, f)
        file.write(str(5)+","+str(receiveTime)+","+str(Vat4)+","+str(Cyt4)+"\n")
        file.flush()
#avg data
        global readingsc4
        global max_samplesc4
        readingc4= Cyt4
        max_samplesc4 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc4.append(readingc4)
        global avgCyt4
        avgCyt4 = mean(readingsc4)
        print(avgCyt4)
#send data        
        if len(readingsc4) >= max_samplesc4: # or strftime("%M", gmtime()) >= time_now4+10:
            print("data sending4")
            sendDataToServer4()
            readingsc4 = []
            readingsv4 = []
            #avgCyt4 = 0
            #time_now4 = strftime("%M", gmtime())

#------------------------------------------------------------------------------

    if msg.topic == "Line5":
        global Vat5
        Vat5 = float(message)
        
#avg data
        global readingsv5
        #global max_samplesv5
        readingv5 = Vat5
        max_samplesv5 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv5.append(readingv5)
        global avgVat5
        avgVat5 = mean(readingsv5)
        
    if msg.topic == "Cyec5":
        global Cyt5
        Cyt5 = float(message)
#part count        
        global P5
        P5=P5+1
        print("PC5 = "+str(P5))
        with open('part5.pickle', 'wb') as f:
            pickle.dump(P5, f)
        file.write(str(6)+","+str(receiveTime)+","+str(Vat5)+","+str(Cyt5)+"\n")
        file.flush()
#avg data
        global readingsc5
        #global max_samplesc5
        readingc5 = Cyt5
        #max_samplesc5 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc5.append(readingc5)
        global avgCyt5
        avgCyt5 = mean(readingsc5)
        print("avgcyt"+str(avgCyt5))
        #print("time"+str(time_now5))
        print(readingsc5)
#send data        
        if len(readingsc5) >= 10: #max_samplesc5: #or strftime("%M", gmtime()) >= time_now5+2:
            print("data sending5")
            sendDataToServer5()
            readingsc5 = []
            readingsv5 = []
            #avgCyt5 = 0
            #avgVat5 = 0
            #time_now5 = strftime("%M", gmtime())
            

#------------------------------------------------------------------------------

    if msg.topic == "Line6":
        global Vat6
        Vat6 = float(message)
#avg data
        global readingsv6
        global max_samplesv6
        readingv6 = Vat6
        max_samplesv6 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsv6.append(readingv6)
        global avgVat6
        avgVat6 = mean(readingsv6)
        
    if msg.topic == "Cyec6":
        global Cyt6
        Cyt6 = float(message)
#part count        
        global P6
        P6=P6+1
        print("PC6 = "+str(P6))
        with open('part6.pickle', 'wb') as f:
            pickle.dump(P6, f)
        file.write(str(7)+","+str(receiveTime)+","+str(Vat6)+","+str(Cyt6)+"\n")
        file.flush()    
#avg data
        global readingsc6
        global max_samplesc6
        readingc6 = Cyt6
        max_samplesc6 = 10

        def mean(nums):
            return float(sum(nums)) / max(len(nums), 1)

        readingsc5.append(readingc6)
        global avgCyt6
        avgCyt5 = mean(readingsc6)
        print(avgCyt6)
#send data        
        if len(readingsc6) >= max_samplesc6: # or strftime("%M", gmtime()) >= time_now6+10:
            print("data sending6")
            sendDataToServer6()
            readingsc6 = []
            readingsv6 = []
            #avgCyt6 = 0
            #time_now6 = strftime("%M", gmtime())

#------------------------------------------------------------------------------


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.55", 1883, 60)
client.loop_forever()
