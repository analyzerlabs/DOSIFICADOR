#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

def openFiles():
		file_id = open("/home/pi/id.txt","r")
		Serie = file_id.readlines()
		Serie = int(Serie[0])
		csvfile = open('data.csv')
		readCSV = csv.reader(csvfile,delimiter=',')
		for row in readCSV:	
			green_led.append(row[11])

    GPIO.setup(int(green_led[Serie]), GPIO.OUT)  # set a port/pin as an input

state = 0
openFiles()
while True:
    state = 1- state
    GPIO.output(int(green_led[Serie]),state)
    time.sleep(2)
