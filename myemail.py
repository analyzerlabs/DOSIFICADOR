import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import time

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

Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'dosificadorlimaem@gmail.com'
sender_pass = 'LimaEM_dosificador'
receiver_address = 'fisicomiguel@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
#The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = '/home/pi/dosis.txt'
attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('*******************************')
print('Mail Sent')
print('*******************************')