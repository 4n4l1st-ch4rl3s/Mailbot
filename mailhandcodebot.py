import smtplib
import stdiomask as stdiomask

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
email = input(f'Enter your email:')
password = stdiomask.getpass(prompt='Enter your password:', mask='*')
receiver = input(f"Enter receipients email address:")
message = input(f'Enter the message: ')
server.login(email, password)
server.sendmail(email, receiver, message)