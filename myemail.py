import smtplib
import csv
import time

gmail_user = 'dosificadorlimaem@gmail.com'
gmail_password = 'LimaEM_dosificador'

file_id= open("/home/pi/file_id.txt","r")
Serie = file_id.readlines()
Serie = int(self.Serie[0])	
ubicacion = []
seccion = []
csvfile = open('data.csv')
readCSV = csv.reader(csvfile,delimiter=';')
	for row in readCSV:
        ubicacion = row[1] 
        seccion = row[2]

sent_from = gmail_user
to = ['fisicomiguel@gmail.com', 'renato.montenegro.ayo@gmail.com']
subject = 'Dosificador '
body = "Envio de actualizacion de datos para el equipo ubicado en" + str(ubicacion[Serie]) +" "str(seccion[Serie])+  
        "\n\n- ATENCION"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print 'Email sent!'
except:
    print 'Something went wrong...'