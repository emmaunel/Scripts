import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_sender = 'aa027n@bhsec.bard.edu'
password = 'sahuarit24'
subject = 'My URLS: URL SHORTENER'
BASE_URL = "http://vurl.com/api.php?"


def sendEmail(results):
    yesOrno = input("Do you want to send the urls to an email(y/n): ")

    if yesOrno == 'y':
        # email_sender = input("Enter your email: ")
        # password = input("Enter your password(Passwords are deleted after email is sent): ")
        target_email = input("Enter the email you want to sent it to.(It could be yours too): ")

        msg = MIMEText(str(results))
        msg['From'] = email_sender
        msg['To'] = target_email
        msg['Subject'] = subject
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_sender, password)
            server.sendmail(email_sender, target_email, msg.as_string())
            server.quit()
            print("Check your email!!!")
            print("Thank you for using me!!!")
        except Exception as e:
            print("Can't send email at this moment\n")
            print("The problem is " + e)
    else:
        print("Thank you for using me!!!")


def shortner(urlsList):
    results = []
    for url in range(len(urlsList)):
        r = requests.get(BASE_URL, "url=" + urlsList[url])
        results.append(r.text)
    print(results)
    sendEmail(results)


if __name__ == "__main__":
    print("Welcome to Url Shortener")
    urls = input("Enter a list of urls(enter n to stop): ")
    print("")

    urlsList = []
    while urls != 'n':
        urlsList.append(urls)
        urls = input("More(enter n to stop): ")

    shortner(urlsList)
