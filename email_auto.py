import smtplib

to = input("Enter the Email address of the recipient:>>>")
message = input('Enter the message you want to send to the recipient:>>>')


def sendEmail(to, message):
    server = smtplib.SMTP('smt.gmail.com',587)
    server.starttls()
    server.login('senderemail','password')
    server.sendmail('senderemail', to , message)
    server.close()

sendEmail(to, message)