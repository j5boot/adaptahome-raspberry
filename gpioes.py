#!/usr/bin/python

import RPi.GPIO as GPIO


class Gpioes :

    def __init__(self) :
	GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)

	GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def setValue(self, jobj):
	out = {}
        if jobj.has_key('id'):
           if jobj['id'] == 1:
              if(jobj["state"]==True):
                 GPIO.output(11, 0)
              else: 
                 GPIO.output(11, 1)

           if jobj['id'] == 2:
              if(jobj["state"]==True):
                 GPIO.output(12, 0)
              else: 
                 GPIO.output(12, 1)

           if jobj['id'] == 3:
              if(jobj["state"]==True):
                 GPIO.output(13, 0)
              else: 
                 GPIO.output(13, 1)

           if jobj['id'] == 4:
              if(jobj["state"]==True):
                 GPIO.output(15, 0)
              else: 
                 GPIO.output(15, 1)

        out['in1'] = GPIO.input(7)
        out['in2'] = GPIO.input(22)
        out['in3'] = GPIO.input(18)
        out['in4'] = GPIO.input(16)
        out['out1'] = GPIO.input(11)
        out['out2'] = GPIO.input(12)
        out['out3'] = GPIO.input(13)
        out['out4'] = GPIO.input(15)
 
        return out


    def getValue(self):
	out = {}
        out['in1'] = GPIO.input(7)
        out['in2'] = GPIO.input(22)
        out['in3'] = GPIO.input(18)
        out['in4'] = GPIO.input(16)
        out['out1'] = GPIO.input(11)
        out['out2'] = GPIO.input(12)
        out['out3'] = GPIO.input(13)
        out['out4'] = GPIO.input(15)
 
        return out
