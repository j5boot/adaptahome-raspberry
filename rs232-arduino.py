#!/usr/bin/python

import serial
import unirest 
import json

estadol = False
estadop = False
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600)

while 1:
   ser.flush()
   data = ser.readline()
   try:
      data = json.loads(data)

      # Luminosidad
      if data.get("l")>300 and not estadol :
         unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 1, "state": True})) 
         estadol = True
      elif data.get("l")<300 and estadol :
         unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 1, "state": False})) 
         estadol = False


      # Proximidad
      if data.get("p")>25 and not estadop :
         unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 2, "state": True})) 
         estadop = True
      elif data.get("p")<25 and estadop :
         unirest.post("http://localhost:8080/setValue/", params=json.dumps({"id": 2, "state": False})) 
         estadop = False

   except:
      pass
   
