import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = str(input("Please input your username: "))
password = getpass.getpass('Please input your password: ')
# receiver = str(input("Please input email address: "))
with open ("receiver_list.txt", "r") as file:
    receiver = file.read().replace('\n','')
# print(receiver.read())
# receiver = open("receiver_list.txt", "r+")
# receiver_list = [i.strip() for i in receiver.readlines()]

message = MIMEMultipart()
message ['From'] = sender
# for addr in receiver:
#     message ['To'] = addr
message ['To'] = receiver
message ['Subject'] = str(input("Input your mail subject: "))

body = str(input("Input your mail body: "))
message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

a = (server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())
server.quit)

for a in receiver (open ("receiver_list.txt", "r")):
    print("Login success")
    print("Email has been sent to ", receiver)

# server.login(sender, password)
# print("Login success")
# server.sendmail(sender, receiver, message.as_string())
# server.quit
# print("Email has been sent to ", receiver)