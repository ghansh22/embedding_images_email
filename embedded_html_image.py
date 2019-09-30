from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

host = "smtp.gmail.com"
port = 587
username = "ghanshyamnetcore"
password = "yourPassword"
from_email = username + "@gmail.com"
to_list = ["gnbaviskar2@gmail.com"]


try:
    email_conn = smtplib.SMTP(host, port)
    email_conn.ehlo()
    email_conn.starttls()
    email_conn.login(username, password)


    msgRoot = MIMEMultipart("related")
    msgRoot["Subject"] = "Sending embedded image in HTML using python2"
    msgRoot["From"] = from_email


    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('This is the alternative plain text message.')
    msgAlternative.attach(msgText)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msgText = MIMEText('<b>Embedded <i>HTML</i> text</b> and an image.<br><img src="cid:pepipost_img2"><br/><br/>I am pepi. The superhero behind the scenes. My special power is inbox delivery...', 'html')
    msgAlternative.attach(msgText)


    # This example assumes the image is in the current directory
    fp = open("image1.j", 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()


    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<pepipost_img2>')
    msgRoot.attach(msgImage)

    # print(msg.as_string())

    email_conn.sendmail(from_email,to_list,msgRoot.as_string())
    email_conn.quit()

except smtplib.SMTPException as e:
    print("error sending message: "+str(e))