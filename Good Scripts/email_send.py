import smtplib

"""Modify"""
def send_email(email, email_to, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email_to, message)
    server.quit()
