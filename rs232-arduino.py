#!/usr/bin/python

import serial
import unirest 
import json

estado = False

while 1:
   ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)
   data = ser.readline()
   
   try: 
      data = int(data.strip())
   except:
      pass

   if data>300 and not estado :
      unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 1, "state": True})) 
      estado = True
   elif data<300 and estado:
      unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 1, "state": False})) 
      estado = False

   
   ser.close()

