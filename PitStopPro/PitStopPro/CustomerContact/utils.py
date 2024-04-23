from .models import Messages
import smtplib
from twilio.rest import Client
from django.conf import settings
# Create your models here.
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "PitStopProTeam@gmail.com"
PASSWORD = "vmoj fuqr ekad klpg"
def sendSMS(to,body):
    client = Client('AC145346e8409f7df08fdd09d8bcba548b', '01dc06c765827e47a49e31ce30fae316')
    message = client.messages.create(
        body=body,
        from_='+18334091034',
        to=to
    )
    return message.sid
def testSMS(to,message):
    recipient = str(to) + CARRIERS["att"]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, str(message))