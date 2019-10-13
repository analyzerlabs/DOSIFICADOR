#!/usr/bin/python
from limaem import *

dosificador = LimaEM(1)
hora = time.strftime("%H")
minuto = time.strftime("%M")
last_time = time.strftime("%S")
while True:
	dosificador.openValve()
	time.sleep(4)
	dosificador.closeValve()
	time.sleep(4)
