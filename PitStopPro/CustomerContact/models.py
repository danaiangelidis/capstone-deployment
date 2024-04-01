from django.db import models
from django.urls import reverse
import uuid
import smtplib

# Create your models here.
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtext.com",
    "sprint": "@messaging.sprintpcs.com"
}
 
EMAIL = "PitStopProTeam@gmail.com"
PASSWORD = "vmoj fuqr ekad klpg"

    

class Messages(models.Model):
    clientName = models.CharField(max_length = 200)
    clientNumber = models.CharField(max_length=10)
    clientEmail = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)
    clientID = models.UUIDField(primary_key = True, default=uuid.uuid4,editable=False)
    
    @property
    def get_html_url(self):
        url = reverse('viewMessage',args=(self.id,))
        return f'<a href="{url}"> {self.clientID}</a>'
        

    def __str__(self):
        # recipient = str(self.clientNumber) + CARRIERS["att"]
        # auth = (EMAIL, PASSWORD)
 
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        # server.login(auth[0], auth[1])
 
        # server.sendmail(auth[0], recipient, str(self.message))
        return "Client Message to {} {}".format(self.clientName, self.clientID)