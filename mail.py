import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("user mailid", "password") 
  
# message to be sent 
message = "hi hello"
  
# sending the mail 
s.sendmail("user mail id", "sender mail id", message) 
  
# terminating the session 
s.quit() 
