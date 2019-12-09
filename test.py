file_intento = open("intento.txt","a")
file_error = open("error.txt","a")



Dia  = 15
Mes  = 10
Ano  = 19
hora   = 3
minuto  = 10
segundo = 10

for j in range (0,30):
    Dia = Dia + 1
    if(Dia == 31):
        Mes = Mes +1 
        Dia = 1
        
    for i in range (0,6):
        hora = hora + 4
        if(hora > 24):
            hora = hora - 24
            H= str(hora)
        elif(hora<10):
            H = "0"+str(hora)
    
         fecha = str(Dia) + "/"+str(Mes)+"/"+str(Ano) + " " + H+ ":10:00"
        
        file_intento.write(fecha + "\t Intento de Dosificacion\n")    
        #file_error.write(fecha + "\t Error : Tiempo de Lectura Excedido , Error Tanque Vacio\n")

file_intento.close()
file_error.close()


