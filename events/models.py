from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=70)
    photo=models.ImageField(upload_to="media/", null=True)
    description = models.CharField(max_length=1420)
    day_date = models.CharField(max_length=60, null=True)
    time =models.CharField(max_length=30,null=True)
    venue = models.CharField(max_length=90, null=True)

    
    def __str__(self):
        return self.name
