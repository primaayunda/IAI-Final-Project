# import smtplib
# sender = "pakaipython@gmail.com"
# password = str(input("Please input your password: "))
# receiever = "sweghooney@gmail.com"
# # subject = "An email via python"
# body = "Halo, this mail was sent via python."

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(sender, password)
# print("Login success")
# server.sendmail(sender, receiever, body)
# print("Email has been sent to ", receiever)

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

message = MIMEMultipart()
message ['From'] = sender
message ['To'] = ",".join(receiver)
message ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
server.sendmail('sender@gmail.com', ["receiver@gmail.com", "receiver@gmail.com"], message.as_string())
server.quit
print("Email has been sent to ", receiver)