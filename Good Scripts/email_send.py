#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_sender = 'aa027n@bhsec.bard.edu'
password = 'sahuarit24'

"""Modify"""

def send_email(email_to, msg, subject):
    msg = MIMEText(str(msg))
    msg['From'] = email_sender
    msg['To'] = email_to
    msg['Subject'] = subject
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_sender, password)
        server.sendmail(email_sender, email_to, msg.as_string())
        server.quit()
        print("Check your email!!!")
        print("Thank you for using me!!!")
    except Exception as e:
        print("Can't send email at this moment\n")
        print("The problem is " + str(e))

if __name__ == '__main__':
    send_to = input("Enter the email: ")
    message = input("Write message: ")
    subject = input("Enter Subject: ")
    send_email(send_to, message, subject)
