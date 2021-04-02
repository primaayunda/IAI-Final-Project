import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender = str(input("Please input your username: "))
password = getpass.getpass('Please input your password: ')
# password = str(input("Please input your password: "))
receiver = open ("receiver_list.txt", "r")
print(receiver.read())
# receiver = [i.strip() for i in receiver.readlines()]
# receiver = str(input("Please input the email address: "))

msg = MIMEMultipart()
msg ['From'] = sender
msg ['To'] = receiver
msg ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
server.sendmail(sender, receiver, message.as_string())
server.quit
print("Email has been sent to ", receiver)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
server.sendmail(sender, "", message.as_string())
server.quit
print("Email has been sent to ", receiver)