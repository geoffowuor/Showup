from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=420)
    date = models.DateTimeField
    
    
def __str__(self):
    return self.name

