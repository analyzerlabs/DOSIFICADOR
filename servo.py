#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD  
GPIO.setup(20, GPIO.IN)  # set a port/pin as an input  
GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input 
GPIO.setup(2, GPIO.OUT)  # set a port/pin as an input 
GPIO.setup(3, GPIO.OUT)  # set a port/pin as an input 
# servo numero 1
min_angle = 55
max_angle = 65
m = GPIO.PWM(10,360)
m.start(max_angle)
vueltas = 0
ant = 0
ant_vueltas = 0
seconds = time.time()
while True:
	angulo = int(input("Ingrese angulo: "))
	GPIO.output(2,False)
	print seconds
	for i in range(0,10):
		time.sleep(0.05)
		m.ChangeDutyCycle(max_angle-i)
	while vueltas< 100:

		i = GPIO.input(20)
		if(i == 1 and ant == 0):
			vueltas += 1
		ant = i
		if(vueltas != ant_vueltas):
			print (vueltas)  #vueltas alamncena las vueltas
		ant_vueltas  = vueltas

	for i in range(0,10):
		time.sleep(0.05)
		m.ChangeDutyCycle(min_angle+i)





