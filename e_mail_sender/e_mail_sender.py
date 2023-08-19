from email.message import EmailMessage
import ssl
import smtplib


email_sender = '18uzumakinaruto18@gmail.com'
email_password = ' ' #email application password https://myaccount.google.com/apppasswords 


email_reciver = ' ' #e-mail address to be sent


subject = "Don't forget to watch bleach"

body = '''
When you watched all episode, Don't forget to talk with friends.
'''


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())