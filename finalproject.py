import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = str(input("Please input your username: "))
password = getpass.getpass('Please input your password: ')

receiver = []
relist = open ("receiver_list.txt", "r")
for i in relist:
    receiver.append(i.replace("\n", ""))

message = MIMEMultipart()
message ['From'] = sender
message ['To'] = i
message ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
print("Login success")
for email in receiver:
    server.sendmail(sender, email, message.as_string())
    print("Email has been sent to ", email)
server.quit()