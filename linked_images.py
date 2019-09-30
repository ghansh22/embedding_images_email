import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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


msg_root = MIMEMultipart("alternative")
msg_root["Subject"] = "Hello there!"
msg_root["From"] = "ghanshyamnetcore@gmail.com"

plain_text = "Test linked immages in email"
html_text = """"\
    <html>
        <head></head>
        <body>
            <b>Embedded <i>HTML</i> text</b> and an image.<br><img src="https://i.ibb.co/sRsFShh/image1.jpg"><br/><br/>I am pepi. The superhero behind the scenes. My special power is inbox delivery...
        </body>
    </html>
"""

part_1 = MIMEText(plain_text, 'plain')
part_2 = MIMEText(html_text, "html")

msg_root.attach(part_1)
msg_root.attach(part_2)

print(msg_root.as_string())

email_conn.sendmail(from_email,to_list,msg_root.as_string())
email_conn.quit()

