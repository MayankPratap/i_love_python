#!python2

# This script sends email to a person in a clean way 

# You have to allow "less secure apps" on your gmail account before running this script.

import smtplib,getpass

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

pw=getpass.getpass()



fromaddr = " XYZ@gmail.com "
toaddr = " ZYX@gmail.com "

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = " Sending mail using terminal, just for fun "

body = " Hey ZYX , whats going on ?? I was learning how to send mail from terminal using Python , So I just mailed you ...  Sorry for disturbing :( "

msg.attach(MIMEText(body,'plain'))



server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,pw)
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()
