import smtplib

sender_email = "your_email@gmail.com"
receiver_email = "receiver@gmail.com"
password = "your_app_password"

message = "Hello, this is an automated email sent using Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

print("Email sent successfully!")
