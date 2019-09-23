#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
import SDL_DS1307

class LimaEM:
	Serie = 1
	nombre = ["PN-RM-01","PN-CA-02","","","","","","","",""]
	volumen     = [ 666, 275, 555, 555, 222, 0  , 555, 222, 0  , 0  , 0  , 0  ]
	error       = [ -5 , 25 , -4 , 10 , 19 , 0  , 0  , 0  , 0  , 0  , 0  , 0  ]
	min_angle   = [ -5 , 10 , 3  , 10 , 19 , 0  , 0  , 0  , 0  , 0  , 0  , 0  ]
	max_angle   = [ -5 , 20 , 17 , 10 , 19 , 0  , 0  , 0  , 0  , 0  , 0  , 0  ]
	delta_angle = [ 14 , 10 , 13 , 12 , 12 , 12 , 12 , 12 , 12 , 12 , 12 , 12 ]
	green_led   = [ 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 , 17 ]
	blue_led    = [  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ,  4 ]
	state       = ["404","401","402","402","402","402","402","402","402","402","402","402"]
	last_update = [ "12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
	                "12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
					"12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
					"12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ]
	
	last_check  = [ "12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
	                "12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
					"12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ,
					"12/24/2018, 04:59:31"  , "12/24/2018, 04:59:31"    , "12/24/2018, 04:59:31"    ]
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
		self.v = int(self.volumen[self.Serie-1] / 2.5) - self.error[self.Serie-1]
		self.last_check[self.Serie-1] = self.file_lastRev.readlines()
		#self.last_check[self.Serie-1] = self.file_lastRev.readlines()
		print ("ultima revision :  ")
		print (self.last_check[self.Serie-1])
		print ("El volumen a medir sera de : " + str(self.volumen[self.Serie-1]) + " mL")
		time.sleep(3)
		GPIO.setmode(GPIO.BCM)            # choose BCM or BOARD
		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setup(20, GPIO.IN)  # set a port/pin as an input
		GPIO.setup(10, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(2, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(3, GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(self.green_led[self.Serie-1], GPIO.OUT)  # set a port/pin as an input
		GPIO.setup(self.blue_led[self.Serie-1], GPIO.OUT)  # set a port/pin as an input
		self.m = GPIO.PWM(10,100)
		self.m.start(self.max_angle[self.Serie-1])
		GPIO.output(self.green_led[self.Serie-1],GPIO.HIGH)
		GPIO.output(self.blue_led[self.Serie-1],GPIO.HIGH)
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
		print self.cont

	def openValve(self):
		for i in range(0,self.delta_angle[self.Serie-1]):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.max_angle[self.Serie-1]-i)

	def closeValve(self):
		for i in range(0,self.delta_angle[self.Serie-1]):
			time.sleep(0.05)
			self.m.ChangeDutyCycle(self.min_angle[self.Serie-1]+i)
		self.m.ChangeDutyCycle(self.min_angle[self.Serie-1]+13)
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
		carnes.closeValve()
		return self.cont

	def blinkLed(self,pin,state):
		GPIO.output(pin,state)

	def printCount(self):
		print self.cont


carnes = LimaEM(1)
hora = time.strftime("%H")
minuto = time.strftime("%M")
last_time = time.strftime("%S")
itsaliveFlag = False
condition = True
signal = 1
while(condition):
	signal = 1 - signal
	carnes.blinkLed(carnes.blue_led[carnes.Serie-1],signal)
	time.sleep(1)
	fecha = time.strftime("%Y-%m-%d %H:%M:%S")
	hora  = time.strftime("%H")
	minuto = time.strftime("%M")
	if(int(hora)%4 == 0 and int(minuto) == 10):
		condition = False


if(int(hora)%4 == 2 and int(minuto) == 10):
	carnes.openFiles()
	print("\t--------------------------------- ")
	print("\t===== EJECUTANDO NUEVA DOSIS ==== ")
	print("\t===== FECHA : " + fecha)
	carnes.openValve()
	vol = carnes.measureVolume(fecha)
	carnes.file_dosis.write("\t"+ fecha + "\t volumen= "+ str(2.5*(vol+carnes.error[carnes.Serie-1])))
	carnes.closeFiles()
	GPIO.setup(10,GPIO.IN)
	GPIO.cleanup()

if(int(minuto)%5 == 0 and itsaliveFlag == True):
	print("saving its alive")
	carnes.openFiles()
	carnes.file_itsalive.write(fecha + "\t Raspberry Encendida\n")
	carnes.closeFiles()
	itsaliveFlag = False

if(int(minuto)%5 == 1 and itsaliveFlag == False):
	itsaliveFlag = True

