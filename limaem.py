#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import csv

class LimaEM:
	Serie = 1
	vol_dosis  = []
	error_vol  = []
	init_dosis = []
	max_angle  = []
	min_angle  = []
	delta_angle= []
	delta_hora = []
	last_update= []
	last_check = []
	last_dosis = []
	state      = []	
	green_led  = []
	blue_led   = []

	# 405 = no operativo
	# 401 = actualizado, sin errores y ejecutando 
	# 402 = no actualizado,sin errores y ejecutando
	# 403 = actualizado , algun error y ejecutando
    # 404 = no actualizado , algun error y ejecutando
	v = 0
	cont = 0
	ant_cont = 0
	esperaNuevaLectura = 0
	def __init__(self,serie):	
		self.openFiles()
		self.Serie = self.file_id.readlines()
	 	self.Serie = int(self.Serie[0])
		

		with open('data.csv') as csvfile:
			readCSV = csv.reader(csvfile,delimiter=';')
			for row in readCSV:
    			self.vol_dosis.append(row[3])
				self.init_dosis.append(row[4])
				self.min_angle.append(row[6])
				self.max_angle.append(row[7])
				self.delta_angle.append(row[8])
				self.error_vol.append(row[9])
				self.last_check.append(row[12])
				self.last_update.append(row[10])
				self.last_dosis.append(row[11])

		self.v = int(self.vol_dosis[self.Serie] / 2.5) - self.error_vol[self.Serie]
		self.last_check[self.Serie] = self.file_lastRev.readlines()
		#self.last_check[self.Serie-1] = self.file_lastRev.readlines()
		print ("ultima revision :  ")
		print (self.last_check[self.Serie])
		print ("El volumen a medir sera de : " + str(self.vol_dosis[self.Serie]) + " mL")
		time.sleep(3)
		GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setup(20, GPIO.IN)  # set a port/pin as an input
		GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(2, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(3, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(self.green_led[self.Serie], GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(self.blue_led[self.Serie], GPIO.OUT)  # set a port/pin as an input
		self.m = GPIO.PWM(10,100)
		self.m.start(self.max_angle[self.Serie])
		GPIO.output(self.green_led[self.Serie],GPIO.HIGH)
		GPIO.output(self.blue_led[self.Serie],GPIO.HIGH)
		time.sleep(2)

	def openFiles(self):
		self.file_lastRev = open("/home/pi/lastRev.txt","r")
		self.file_id = open("/home/pi/id.txt","r")
		self.file_intento = open("/home/pi/intento.txt","a")
		self.file_dosis = open("/home/pi/dosis.txt","a")
		self.file_error = open("/home/pi/error.txt","a")
		self.file_itsalive = open("/home/pi/itsalive.txt","a")

	def closeFiles(self):
		self.file_intento.close()
		self.file_dosis.close()
		self.file_error.close()
		self.file_itsalive.close()

	def counter(self,pin):
		self.cont += 1
		print (self.cont)

	def openValve(self):
		for i in range(0,self.delta_angle[self.Serie]):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.max_angle[self.Serie]-i)

	def closeValve(self):
		for i in range(0,self.delta_angle[self.Serie]):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.min_angle[self.Serie]+i)
		self.m.ChangeDutyCycle(self.min_angle[self.Serie]+self.delta_angle[self.Serie]+1)
		self.m.stop()

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
		self.closeValve()
		return self.cont

	def blinkLed(self,pin,state):
		GPIO.output(pin,state)

	def printCount(self):
		print (self.cont)

	def printRevision(self):
		print ("----> ultima revision:  " + str(self.last_check[self.Serie]))

dosificador = LimaEM(1)
dosificador.printRevision()

hora = time.strftime("%H")
minuto = time.strftime("%M")
last_time = time.strftime("%S")
itsaliveFlag = False
condition = True
signal = 1
while(condition):
	signal = 1 - signal
	dosificador.blinkLed(dosificador.blue_led[dosificador.Serie],signal)
	time.sleep(1)
	fecha = time.strftime("%Y-%m-%d %H:%M:%S")
	hora  = time.strftime("%H")
	minuto = time.strftime("%M")
	if(int(hora)%4 == 3 and int(minuto) == 10):
		condition = False


if(int(hora)%4 == 3 and int(minuto) == 10):
	dosificador.openFiles()
	print("\t--------------------------------- ")
	print("\t===== EJECUTANDO NUEVA DOSIS ==== ")
	print("\t===== FECHA : " + fecha)
	dosificador.openValve()
	vol = dosificador.measureVolume(fecha)
	dosificador.file_dosis.write("\t"+ fecha + "\t volumen= "+ str(2.5*(vol+dosificador.error[dosificador.Serie])))
	dosificador.closeFiles()
	GPIO.setup(10,GPIO.IN)
	GPIO.cleanup()

if(int(minuto)%5 == 0 and itsaliveFlag == True):
	print("saving its alive")
	dosificador.openFiles()
	dosificador.file_itsalive.write(fecha + "\t Raspberry Encendida\n")
	dosificador.closeFiles()
	itsaliveFlag = False

if(int(minuto)%5 == 1 and itsaliveFlag == False):
	itsaliveFlag = True

