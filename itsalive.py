#!/usr/bin/python

import time
import datetime
import curses

def openFiles():
    file_itsAlive = open("/home/pi/itsalive.txt","a")
    fecha = time.strftime("%m/%d/%Y, %H:%M:%S")
    file_itsAlive.write(fecha + "\t" + "activo \n")
    print("***************************************")
    print("Comprobando si el equipo esta Encendido")
    print("***************************************")
    return 0
    
openFiles()