#import smtplibrary
import smtplib

to = input("Enter the Email address of the recipient:>>>") #for Taking inputs from user 
message = input('Enter the message you want to send to the recipient:>>>')


def sendEmail(to, message):           #define function
    server = smtplib.SMTP('smt.gmail.com',587) # setting up host
    server.starttls()  # starting tls service
    server.login('senderemail','password')   #here fill login information 
    server.sendmail('senderemail', to , message) # here is sending function 
    
    server.close()   # closing session

sendEmail(to, message)   # calling the function
