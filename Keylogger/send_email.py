# Import Required Libraries
# Important Library For a send keys to email
import smtplib, ssl

# Define the function

def sendEmail(message):
	smtp_server = "smtp.gmail.com"
	port = 587 
	sender_email = "rohit.gaware90@gmail.com"
	password = "qcekmkggpmuplagf"
	receiver_email = "rohit.gaware90@gmail.com"

	context = ssl.create_default_context()

	try:
	    server = smtplib.SMTP(smtp_server,port)
	    server.ehlo() 
	    server.starttls(context=context) 
	    server.ehlo()
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)
	   
	except Exception as e:
	    print(e)
	finally:
	    server.quit()