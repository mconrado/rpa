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

msg["Subject"] = "Venha conhecer o nosso restaurante!!!"

body = """Inauguração do nosso restaurante esta noite, venha conhecer."""

msg.attach(MIMEText(body, "plain"))

filename = "panfleto.pdf"

anexo = open("panfleto.pdf", "rb")

p = MIMEBase("application", "octet-stream")

p.set_payload((anexo).read())

encoders.encode_base64(p)

p.add_header("Content-Disposition", "attachment; filename= %s" % filename)

msg.attach(p)

s = smtplib.SMTP(config("HOST_SMTP"), config("HOST_SMTP_PORT"))

s.starttls()

s.login(fromaddr, config("HOST_PASSWORD"))

text = msg.as_string()

s.sendmail(fromaddr, toaddr.split(","), text)

s.quit()
