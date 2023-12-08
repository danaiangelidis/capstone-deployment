from django.db import models
from django.urls import reverse
# Create your models here.
#Used to add event to Calendar
class Event(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return 'Event #{}'.format(self.id)