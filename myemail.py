import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import time

print("Enviando Email")
file_id= open("/home/pi/id.txt","r")
Serie = file_id.readlines()
Serie = int(Serie[0])	
ubicacion = []
seccion = []
csvfile = open('data.csv')
readCSV = csv.reader(csvfile,delimiter=';')
for row in readCSV:
        ubicacion.append(row[1]) 
        seccion.append(row[2])


mail_content = '''
Email sent from ''' + str(ubicacion[Serie]) + " " + str(seccion[Serie])+'''  \n

Hola,
Este email esta siendo enviado como parte de la revision
Ubiacion : ''' +str(ubicacion[Serie]) +'''\n Sector: ''' + str(seccion[Serie]) + "\n Thank you"

files = "/home/pi"
filenames = [os.path.join(files, f) for f in os.listdir(files)]

#The mail addresses and password
sender_address = 'dosificadorlimaem@gmail.com'
sender_pass = 'LimaEM_dosificador'
receiver_address = 'fisicomiguel@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Revision y Log Equipo ubicado en ' + str(ubicacion[Serie]) + '  sector : ' + str(seccion[Serie])
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

#attach_file_name = '/home/pi/dosis.txt'
#attach_file = open(attach_file_name, 'rb') # Open the file as binary mode

# adjunto numero 1 = lastrev.txt
part = MIMEBase('application', 'octet-stream')
part.set_payload(open("/home/pi/lastRev.txt", 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="/home/pi/lastRev.txt"')
message.attach(part)#Create SMTP session for sending the mail

# adjunto numero 2 = dosis.txt
part = MIMEBase('application', 'octet-stream')
part.set_payload(open("/home/pi/dosis.txt", 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="/home/pi/dosis.txt"')
message.attach(part)#Create SMTP session for sending the mail

# adjunto numero 3 = error.txt
part = MIMEBase('application', 'octet-stream')
part.set_payload(open("/home/pi/error.txt", 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="/home/pi/error.txt"')
message.attach(part)#Create SMTP session for sending the mail


# adjunto numero 4 = itsalive.txt
part = MIMEBase('application', 'octet-stream')
part.set_payload(open("/home/pi/itsalive.txt", 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="/home/pi/itsalive.txt"')
message.attach(part)#Create SMTP session for sending the mail


# adjunto numero 5 = intento.txt
part = MIMEBase('application', 'octet-stream')
part.set_payload(open("/home/pi/intento.txt", 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="/home/pi/intento.txt"')
message.attach(part)#Create SMTP session for sending the mail

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('*******************************')
print('Mail Sent')
print('*******************************')
