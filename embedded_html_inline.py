# Python code to illustrate Sending mail with attachments 
# from your Gmail account 

# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from_addr = "ghanshyamnetcore@gmail.com"
to_addr = "gnbaviskar2@gmail.com"

# instance of MIMEMultipart 
the_msg = MIMEMultipart() 

# storing the senders email address 
the_msg['From'] = from_addr 

# storing the receivers email address 
the_msg['To'] = to_addr 

# storing the subject 
the_msg['Subject'] = "Inline embedded image"

# string to store the body of the mail 
body = "I am pepi. The superhero behind the scenes. My special power is inbox delivery..."

# attach the body with the_msg instance 
the_msg.attach(MIMEText(body, 'plain')) 

# open the file to be sent 
filename = "image1.jpg"
attachment = open(filename, "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'the_msg' 
the_msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login(from_addr, "yourPassword") 

# Converts the Multipart the_msg into a string 
text = the_msg.as_string() 

# sending the mail 
s.sendmail(from_addr, to_addr, text) 

# terminating the session 
s.quit() 
