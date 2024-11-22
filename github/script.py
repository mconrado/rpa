import smtplib
import requests
from decouple import config

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

response = requests.get("https://api.github.com/users/mconrado")
data = response.json()


fromaddr = config("HOST_USER")
toaddr = config("SEND_TO")

msg = MIMEMultipart()

msg["From"] = fromaddr

msg["To"] = toaddr

msg["Subject"] = "Informações recebidas via API GitHub"

body = "Seguidores: %s\n Seguindo: %s\n" % (data["followers"], data["following"])

msg.attach(MIMEText(body, "plain"))


s = smtplib.SMTP(config("HOST_SMTP"), config("HOST_SMTP_PORT"))

s.starttls()

s.login(fromaddr, config("HOST_PASSWORD"))

text = msg.as_string()

s.sendmail(fromaddr, toaddr.split(","), text)

s.quit()
