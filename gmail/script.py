import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = ""
toaddr = ""

msg = MIMEMultipart()

msg["From"] = fromaddr

msg["To"] = toaddr

msg["Subject"] = "E-mail de teste"

body = """E-mail enviado do nosso robo."""

msg.attach(MIMEText(body, "plain"))

s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

s.login(fromaddr, "")

text = msg.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()
