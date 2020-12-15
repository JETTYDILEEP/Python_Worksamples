import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("dileepchinna333@gmail.com", "Dileep!@2309") 
  
# message to be sent 
message = "hi hello"
  
# sending the mail 
s.sendmail("dileepchinna333@gmail.com", "jettydileepreddy@gmail.com", message) 
  
# terminating the session 
s.quit() 
