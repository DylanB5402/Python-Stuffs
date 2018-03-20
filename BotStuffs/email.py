import smtplib
import imapclient
import pyzmail
import pprint 

def email():
    email = smtplib.SMTP('smtp.gmail.com', 587)
    email.ehlo()
    email.starttls()
    #password = input('Password:')
    email.login('dylanb5402@gmail.com', 'supertaco9000')
    email.sendmail('dylanb5402@gmail.com', 'd.barva5402@gmail.com', 'Subject: Stupid Head. \nU stupid')
    email.quit()
    
def readmail():
    reader = imapclient.IMAPClient('imap.gmail.com', ssl = False)
    reader.login('dylanb5402@gmail.com', 'supertaco9000')
    folders =  pprint.pprint(reader.list_folders())
    print folders