#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime

def openFiles():
		file_localRev = open("/home/pi/local_rev.txt","w")
        fecha = time.strftime("%Y-%m-%d %H:%M:%S")
        file_localRev.write(fecha)
        print "Inicio de nueva revision "
        print (fecha)
        return 0


openfiles()

