#!/usr/bin/python
from limaem import *

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
	dosificador.blinkLed(int(dosificador.blue_led[dosificador.Serie]),signal)
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
	dosificador.file_dosis.write("\t"+ fecha + "\t volumen= "+ str(2.5*(vol+int(dosificador.error_vol[dosificador.Serie])))+"\n")
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