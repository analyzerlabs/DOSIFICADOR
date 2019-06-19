#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(20, GPIO.IN)  # set a port/pin as an input  
GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input 
m = GPIO.PWM(10,360)
m.start(0)
vueltas = 0
ant = 0
ant_vueltas = 0
seconds = time.time()
while True:
	#angulo = int(input("Ingrese angulo: "))	
	
	print seconds
	#while vueltas< 100:
	for i in range(0,45):
		time.sleep(0.05)
		m.ChangeDutyCycle(i)
		#i = GPIO.input(20)
		#if(i == 1 and ant == 0):
		#	vueltas += 1
		#ant = i
		#if(vueltas != ant_vueltas):
		#	print (vueltas)  #vueltas alamncena las vueltas
		#ant_vueltas  = vueltas
	time.sleep(2)
	for i in range(0,45):
		time.sleep(0.05)
		m.ChangeDutyCycle(45-i)
	time.sleep(2)
		




