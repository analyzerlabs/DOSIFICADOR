import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        ubicacion = row[1] 
        seccion = row[2]

email_user = 'dosificadorlimaem@gmail.com'
email_password = 'LimaEM_dosificador'
email_send = ['fisicomiguel@gmail.com', 'renato.montenegro.ayo@gmail.com']

subject = 'Dosificador'+ str(ubicacion[Serie]) +" "+str(seccion[Serie])

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename='data.csv'
attachment  = open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        server.quit()
        print 'Email sent!'
except:
        print 'Something went wrong...'