#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import SDL_DS1307


class LimaEM:
	v = 0
	cont = 0
	ant_cont = 0
	def __init__(self,volumen):
#		ds1307.write_now()
		self.v = int(volumen / 2.5)
		GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
		GPIO.cleanup()
		GPIO.setup(20, GPIO.IN)  # set a port/pin as an input
		GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(2, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(3, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(4, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(17, GPIO.OUT)  # set a port/pin as an input
#		GPIO.add_event_detect( 20 , GPIO.FALLING  , callback = self.counter)
		self.m = GPIO.PWM(10,100)
		self.min_angle = 7
		self.max_angle = 18
		self.m.start(self.max_angle)
		self.file_dosis = open("dosis1.txt","a")
		self.file_error = open("error1.txt","a")
		GPIO.output(4,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		

	def counter(self,pin):
		self.cont += 1
		print self.cont

	def openValve(self):
		for i in range(0,12):
			time.sleep(0.03)
			self.m.ChangeDutyCycle(self.max_angle-i)

	def closeValve(self):
		for i in range(0,12):
			time.sleep(0.03)
			self.m.ChangeDutyCycle(self.min_angle+i)
		self.m.stop()
		
	def measureVolume(self,fecha):
		t0 = time.time()
		while GPIO.input(20) != 0 :
			print("wrong")
			time.sleep(0.0001)
			# el volumen se define aqui 
			if(t1 - t0 >= 10):
				t0 = t1
				self.file_error.write(fecha + "\t Error , Excedio el tiempo de Apertura de la LLave\n")
				break
		lastMeasure = GPIO.input(20)
		while self.cont < v :
			if(GPIO.input(20)==1  and lastMeasure == 0):
				self.cont += 1
				while(GPIO.input(20) != 0):
					print (" ")
				self.ant_cont = self.cont
			t1=time.time()
			if(t1 - t0 >= 10):
				print("\t\t puede haber error  en " + str(10-t1+t0))
				t0 = t1
				self.file_error.write(fecha + "\t Error , Excedio el tiempo de Apertura de la LLave\n")
				break
		self.cont = 0
		self.ant_cont = 0
		self.file_dosis.write(fecha + "\t Intento de Dosificacion \n")

	def blinkLed(self,pin,state):
		GPIO.output(pin,state)

	def printCount(self):
		print self.cont

		
def calcSeconds(t):
	x = time.strftime("%S")
	if(abs(y-x) == t):
		print "kek"
	else:
		y = time.strftime("%S")
		
carnes = LimaEM(150)
hora = time.strftime("%H")
minuto = time.strftime("%M")
last_time = time.strftime("%S")
while True:
	if(int(hora)%4 == 0 and int(minuto) == 25):
		fecha = time.strftime("%Y-%m-%d %H:%M:%S") 
		carnes.openValve()
		carnes.measureVolume(fecha)
		carnes.closeValve()
		time.sleep(100)
	hora = time.strftime("%H")
	minuto = time.strftime("%M")
	



