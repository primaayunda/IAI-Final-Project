import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = str(input("Please input your username: "))
password = getpass.getpass('Please input your password: ')

receiver = open ("receiver_list.txt", "r")
for i in receiver:
    i = i.replace("\n", "")
    l = (i.split(" "))
    print(l)

message = MIMEMultipart()
message ['From'] = sender
message ['To'] = l
message ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
for email in i:
    server.sendmail(sender, l, message.as_string())
server.quit()
print("Email has been sent to ", l)