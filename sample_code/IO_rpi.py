#!/usr/bin/env python
# This is a basic input output debug script designed to take advantage of the GPIO features of the PI
# This script has been written for Campus Party Europe 2013
# Written By: Fei Manheche
# Dated: 03/09/2013
# Copyright (c) 2013 Robobo Inc., 
# Licensed under the MIT License (the "License");

import time
#import dependency library (ensure you have installed the deb file as per docs)
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

#Welcome Message
print ("#######################################################\n")
print ("#####    Welcome to GPIO IoT V1.0 Demo             ####\n")
print ("#####     Commands: on, off, blink, input, iot     ####\n")
print ("##########Written#By#Fei :)############################\n")
#Setting GPIO Pin 11 As LED Control Pin
LED_Pin = 11
#Setting GPIO Pin 7 As input pin
push_button = 7
##Set Blink Frequency
frequency = 0.5

#CleanThings Up at the beginning of the script
GPIO.setwarnings(False)
GPIO.cleanup()

#Setup GPIO pins
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(LED_Pin, GPIO.OUT)
	GPIO.setup(push_button, GPIO.IN)

#Control Functions
def Output(status):
	if status == 'on':
		GPIO.output(LED_Pin, GPIO.HIGH)
		print ("Turned ON")
	elif status == 'off':
		GPIO.output(LED_Pin, GPIO.LOW)
		print ("Turned OFF")
	elif status == 'input':
		#User pushed a button
		listenButton()
	elif status == "blink":
		p = GPIO.PWM(LED_Pin, frequency)
		p.start(1)
		raw_input('Enter stop to stop blinking:')   
		p.stop()
		GPIO.cleanup()
	else:
		print ("No Action chosen")

#Input listner
def listenButton():
	while GPIO.input(push_button) == GPIO.LOW:
	    time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        print 'Button Pressed :)'

from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
def iot():
	# The web server.
	class MyHandler(SimpleHTTPRequestHandler):
	  def do_POST(self):
	    if self.path == '/on':
		print "Got It"	
		Output('on')
	    elif self.path =='/off':
		print "Got It"
		Output('off')
	    return
	server = HTTPServer(('', 8081), MyHandler).serve_forever()

#choose action:
while 1:
	GPIO.cleanup()
	setup()
	userAction = raw_input('Enter LED Control Option: ')
	if userAction == 'exit':
		exit()
	if userAction == 'iot':
		iot()
	Output(userAction)



