import smtplib
import stdiomask as stdiomask
from email.message import EmailMessage


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
mail = input(f'Enter your email: ')
password = stdiomask.getpass(prompt='Enter your password: ', mask='*')
server.login(mail, password)
receiver = input(f"Enter receiver's email: ")
subject = input(f'Enter the Subject of the email: ')
message = input(f'Enter the message of the email you want to send: ')
email = EmailMessage()
email['From'] = mail
email['To'] = receiver
email['Subject'] = subject
email.set_content(message)
server.send_message(email)
