#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

def openFiles():
    file_localRev = open("/home/pi/localRev.txt","w")
    fecha = now.strftime("%m/%d/%Y, %H:%M:%S")
    file_localRev.write(fecha)
    print "Inicio de nueva revision "
    print (fecha)
    return 0


openfiles()

