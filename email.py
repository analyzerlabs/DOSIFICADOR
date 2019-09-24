import smtplib

gmail_user = 'fisicomiguel@gmail.com'
gmail_password = 'Fisico_de_la_uni_1'

sent_from = gmail_user
to = ['fisicomiguel@gmail.com', 'miguelquispecastro@uni.pe']
subject = 'OMG Super Important Message'
body = 'Hey, whats up? \n\n- You'

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