import smtplib
from decouple import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from corpo_email import corpo_email

fromaddr = config("HOST_USER")
toaddr = config("SEND_TO")

msg = MIMEMultipart()

msg["From"] = fromaddr

msg["To"] = toaddr

msg["Subject"] = "Videos Aulas Grátis!!!"

part1 = MIMEText(corpo_email, "html")

msg.attach(part1)


s = smtplib.SMTP(config("HOST_SMTP"), config("HOST_SMTP_PORT"))

s.starttls()

s.login(fromaddr, config("HOST_PASSWORD"))

text = msg.as_string()

s.sendmail(fromaddr, toaddr.split(","), text)

s.quit()
