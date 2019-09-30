import smtplib

host = "smtp.gmail.com"
port = 587
username = "ghanshyamnetcore"
password = "yourPassword"
from_email = username + "@gmail.com"
to_list = ["gnbaviskar@gmail.com","gnbaviskar2@gmail.com"]


email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email,to_list,"A simple message")
email_conn.quit()