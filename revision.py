#!/usr/bin/python
#import RPi.GPIO as GPIO
import time
import datetime
import curses 

def menu(stdscr):
    curses.cur_set(0)
    h,w= stdscr.getmax(yx)
    text = "INICIO"
    x=w//2 - len(text)//2 
    y=h//2
    stdscr.addstr(y,x,text)
    stdscr.refresh()
    time.sleep(3)

def openFiles():
    file_lastRev = open("/home/pi/lastRev.txt","w")
    fecha = time.strftime("%m/%d/%Y, %H:%M:%S")
    file_lastRev.write(fecha)
    print "Inicio de nueva revision "
    print (fecha)
    return 0
    
menu()
openFiles()

