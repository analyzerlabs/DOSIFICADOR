#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import csv

green_led = []
state = 0
veces = 0

file_id = open("/home/pi/id.txt","r")
Serie = file_id.readlines()
Serie = int(Serie[0])
csvfile = open("/home/pi/DOSIFICADOR/data.csv")
readCSV = csv.reader(csvfile,delimiter=',')
for row in readCSV:	
	green_led.append(row[12])

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(green_led[Serie]), GPIO.OUT)  # set a port/pin as an input

GPIO.output(int(green_led[Serie]),0)
