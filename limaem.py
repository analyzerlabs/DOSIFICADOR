#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import SDL_DS1307


class LimaEM:
	Serie = 1
	volumen = [666,276,555,555,222,0,555,222,0,0,0,0]
	error = [-5,25,-4,10,19,0,0,0,0,0,0,0]
	min_angle = [-5,25,5,10,19,0,0,0,0,0,0,0]
	max_angle = [-5,25,18,10,19,0,0,0,0,0,0,0]
	v = 0
	cont = 0
	ant_cont = 0
	esperaNuevaLectura = 0
	def __init__(self,serie):
		self.Serie = serie
		self.v = int(self.volumen[self.Serie-1] / 2.5) - self.error[self.Serie-1] 
		print ("El volumen a medir sera de : " + str(self.volumen[self.Serie-1]) + " mL")
		time.sleep(3)
		GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setup(20, GPIO.IN)  # set a port/pin as an input
		GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(2, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(3, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(4, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(17, GPIO.OUT)  # set a port/pin as an input
		self.m = GPIO.PWM(10,100)
		self.m.start(self.max_angle[self.Serie-1])
		self.openFiles()
		GPIO.output(4,GPIO.HIGH)
		GPIO.output(17,GPIO.HIGH)
		
	def openFiles(self):
		self.file_intento = open("intento1.txt","a")
		self.file_dosis = open("dosis1.txt","a")
		self.file_error = open("error1.txt","a")
		self.file_itsalive = open("itsalive1.txt","a")
	
	def closeFiles(self):
		self.file_intento.close()
		self.file_dosis.close()
		self.file_error.close()
		self.file_itsalive.close()
		
	def counter(self,pin):
		self.cont += 1
		print self.cont

	def openValve(self):
		for i in range(0,12):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.max_angle[self.Serie-1]-i)

	def closeValve(self):
		for i in range(0,12):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.min_angle[self.Serie-1]+i)
		
		
	def measureVolume(self,fecha):
		self.file_intento.write(fecha + "\t Intento de Dosificacion \n")
		t0 = time.time()
		while GPIO.input(20) != 0 :
			time.sleep(0.0001)
			t1 = time.time()
			# el volumen se define aqui 
			if(t1 - t0 >= 20):
				print("\t===== Error : Tiempo de Lectura Excedido , Error Tanque Vacio")
				t0 = t1
				self.file_error.write(fecha + "\t Error : Tiempo de Lectura Excedido , Error Tanque Vacio\n")
				self.closeValve()
				return self.cont
		lastMeasure = GPIO.input(20)
		t0 = time.time()
		while self.cont < self.v :
			if(GPIO.input(20)==1  and lastMeasure == 0):
				self.cont += 1
				while(GPIO.input(20) != 0):
					self.esperaNuevaLectura +=0
				self.ant_cont = self.cont
				self.esperaNuevaLectura = 0
			t1=time.time()
			if(t1 - t0 >= 20):
				print("\t===== Error : Tiempo de Lectura Excedido , Error Tanque Agotado")
				t0 = t1
				self.file_error.write(fecha + "\t Error : Tiempo de Lectura Excedido , Error Tanque Agotado\n")
				self.closeValve()
				return self.cont
		self.ant_cont = 0
		carnes.closeValve()
		return self.cont
		
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
		
carnes = LimaEM(1)
hora = time.strftime("%H")
minuto = time.strftime("%M")
last_time = time.strftime("%S")
itsaliveFlag = False

fecha = time.strftime("%Y-%m-%d %H:%M:%S") 
hora = time.strftime("%H")
minuto = time.strftime("%M")	
if(int(hora)%1 == 0 and int(minuto)%1 ==0):
	carnes.openFiles()
	print("\t--------------------------------- ")
	print("\t===== EJECUTANDO NUEVA DOSIS ==== ")
	print("\t===== FECHA : " + fecha) 
	carnes.openValve()
	vol = carnes.measureVolume(fecha)
	
	carnes.closeFiles()
	time.sleep(60)
if(int(minuto)%5==0 and itsaliveFlag == True):
	print("saving its alive")
	carnes.openFiles()
	carnes.file_itsalive.write(fecha + "\t Estor vivo PRR\n")
	carnes.closeFiles()
	itsaliveFlag = False
	
if(int(minuto)%5==1 and itsaliveFlag == False):
	itsaliveFlag = True
	
