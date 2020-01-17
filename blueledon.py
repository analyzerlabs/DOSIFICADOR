#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import csv

blue_led = []
state = 0
veces = 0

file_id = open("/home/pi/id.txt","r")
Serie = file_id.readlines()
Serie = int(Serie[0])
csvfile = open("/home/pi/DOSIFICADOR/data.csv")
readCSV = csv.reader(csvfile,delimiter=',')
for row in readCSV:	
	blue_led.append(row[11])

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(blue_led[Serie]), GPIO.OUT)  # set a port/pin as an input

while veces < 30:
    veces = veces + 1
    state = 1- state
    GPIO.output(int(blue_led[Serie]),state)
    time.sleep(0.5)