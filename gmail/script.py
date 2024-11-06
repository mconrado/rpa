import smtplib
from decouple import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = config("HOST_USER")
toaddr = config("SEND_TO")

msg = MIMEMultipart()

msg["From"] = fromaddr

msg["To"] = toaddr

msg["Subject"] = "E-mail de teste"

body = """E-mail enviado do nosso robo."""

msg.attach(MIMEText(body, "plain"))

s = smtplib.SMTP(config("HOST_SMTP"), config("HOST_SMTP_PORT"))

s.starttls()

s.login(fromaddr, config("HOST_PASSWORD"))

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
