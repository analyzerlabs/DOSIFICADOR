# ! / usr / bin / python
importar RPi. GPIO  como  GPIO
tiempo de importación
fecha y hora de importación
importar  SDL_DS1307


clase  LimaEM :
	Serie =  1
	volumen = [ 666 , 276 , 555 , 555 , 222 , 0 , 555 , 222 , 0 , 0 , 0 , 0 ]
	error = [ - 5 , 25 , - 4 , 10 , 19 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
	v =  0
	cont =  0
	ant_cont =  0
	esperaNuevaLectura =  0
	def  __init__ ( self , serie ):
		self .Serie = serie
# 		ds1307.write_now ()
		self .v =  int ( self .volumen [ self .Serie - 1 ] /  2.5 ) -  self .error [ self .Serie - 1 ]
		print ( " El volumen a medir sera de: "  +  str ( self .volumen [ self .Serie - 1 ]) +  " mL " )
		tiempo de dormir ( 3 )
		GPIO .setmode ( GPIO . BCM )             # elija BCM o BOARD
		GPIO .setwarnings ( Falso )
		GPIO .cleanup ()
		GPIO .setup ( 20 , GPIO . IN )   # establece un puerto / pin como entrada
		GPIO .setup ( 10 , GPIO . OUT )   # establece un puerto / pin como entrada
		GPIO .setup ( 2 , GPIO . OUT )   # establece un puerto / pin como entrada
		GPIO .setup ( 3 , GPIO . OUT )   # establece un puerto / pin como entrada
		GPIO .setup ( 4 , GPIO . OUT )   # establece un puerto / pin como entrada
		GPIO .setup ( 17 , GPIO . OUT )   # establece un puerto / pin como entrada
# 		GPIO.add_event_detect (20, GPIO.FALLING, callback = self.counter)
		self .m =  GPIO .PWM ( 10 , 100 )
		self .min_angle =  3
		self .max_angle =  15
		self .m.start ( self .max_angle)
		self .openFiles ()
		GPIO .output ( 4 , GPIO . ALTO )
		GPIO .output ( 17 , GPIO . ALTO )
		
	def  openFiles ( self ):
		self .file_dosis =  abierto ( " dosis1.txt " , " a " )
		self .file_error =  open ( " error1.txt " , " a " )
		self .file_itsalive =  open ( " itsalive1.txt " , " a " )
	
	def  closeFiles ( self ):
		self .file_dosis.close ()
		self .file_error.close ()
		self .file_itsalive.close ()
		
	 contador de def ( auto , pin ):
		self .cont + =  1
		print  self .cont

	def  openValve ( self ):
		para i en  rango ( 0 , 12 ):
			tiempo de sueño ( 0.05 )
			self .m.ChangeDutyCycle ( self .max_angle - i)

	def  closeValve ( self ):
		para i en  rango ( 0 , 12 ):
			tiempo de sueño ( 0.05 )
			self .m.ChangeDutyCycle ( self .min_angle + i)
		
		
	def  measureVolume ( self , fecha ):
		self .file_dosis.write (fecha +  " \ t Intento de Dosificacion \ n " )
		t0 = time.time ()
		mientras  GPIO .input ( 20 ) ! =  0 :
			time.sleep ( 0.0001 )
			t1 = time.time ()
			# el volumen se define aqui
			si (t1 - t0 > =  20 ):
				print ( " \ t ===== Error: Tiempo de lectura excedido, error Tanque Vacio " )
				t0 = t1
				self .file_error.write (fecha +  " \ t Error: Tiempo de Lectura Excedido, Error Tanque Vacio \ n " )
				self .closeValve ()
				volver  0
		lastMeasure =  GPIO .input ( 20 )
		t0 = time.time ()
		mientras  self .cont <  self .v:
			if ( GPIO .input ( 20 ) == 1   y lastMeasure ==  0 ):
				self .cont + =  1
				while ( GPIO .input ( 20 ) ! =  0 ):
					auto .esperaNuevaLectura + = 0
				self .ant_cont =  self .cont
				self .esperaNuevaLectura =  0
			t1 = time.time ()
			si (t1 - t0 > =  20 ):
				print ( " \ t ===== Error: Tiempo de Lectura Excedido, Error Tanque Agotado " )
				t0 = t1
				self .file_error.write (fecha +  " \ t Error: Tiempo de Lectura Excedido, Error Tanque Agotado \ n " )
				self .closeValve ()
				volver  0
		self .cont =  0
		self .ant_cont =  0
		carnes.closeValve ()
		
	def  blinkLed ( auto , pin , estado ):
		GPIO .output (pin, estado)

	def  printCount ( self ):
		print  self .cont

		
def  calcSeconds ( t ):
	x = time.strftime ( " % S " )
	if ( abs (y - x) == t):
		imprimir  " kek "
	otra cosa :
		y = time.strftime ( " % S " )
		
carnes = LimaEM ( 1 )
hora = time.strftime ( " % H " )
minuto = time.strftime ( " % M " )
last_time = time.strftime ( " % S " )
itsaliveFlag =  False
mientras  cierto :
	fecha = time.strftime ( " % Y-% m- % d % H:% M:% S " )
	hora = time.strftime ( " % H " )
	minuto = time.strftime ( " % M " )	
	if ( int (hora) % 1  ==  0  e  int (minuto) % 1  == 0 ):
		carnes.openFiles ()
		print ( " \ t --------------------------------- " )
		print ( " \ t ===== EJECUTANDO NUEVA DOSIS ==== " )
		print ( " \ t ===== FECHA: "  + fecha)
		carnes.openValve ()
		carnes.measureVolume (fecha)
		carnes.closeFiles ()
		tiempo de dormir ( 60 )
	if ( int (minuto) % 5 == 0  y itsaliveFlag ==  True ):
		print ( " salvando su vida " )
		carnes.openFiles ()
		carnes.file_itsalive.write (fecha +  " \ t Estor vivo PRR \ n " )
		carnes.closeFiles ()
		itsaliveFlag =  False
		
	if ( int (minuto) % 5 == 1  y itsaliveFlag ==  False ):
		itsaliveFlag =  True
