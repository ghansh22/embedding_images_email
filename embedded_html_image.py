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


    msg_root = MIMEMultipart("related")
    msg_root["Subject"] = "Sending embedded image in HTML using python2"
    msg_root["From"] = from_email


    msg_alternative = MIMEMultipart('alternative')
    msg_root.attach(msg_alternative)

    msg_text = MIMEText('This is the alternative plain text message.')
    msg_alternative.attach(msg_text)

    # We reference the image in the IMG SRC attribute by the ID we give it below
    msg_text = MIMEText('<b>Embedded <i>HTML</i> text</b> and an image.<br><img src="cid:pepipost_img2"><br/><br/>I am pepi. The superhero behind the scenes. My special power is inbox delivery...', 'html')
    msg_alternative.attach(msg_text)


    # This example assumes the image is in the current directory
    fp = open("image1.jpg", 'rb')
    msg_image = MIMEImage(fp.read())
    fp.close()


    # Define the image's ID as referenced above
    msg_image.add_header('Content-ID', '<pepipost_img2>')
    msg_root.attach(msg_image)

    # print(msg.as_string())

    email_conn.sendmail(from_email,to_list,msg_root.as_string())
    email_conn.quit()

except smtplib.SMTPException as e:
    print("error sending message: "+str(e))