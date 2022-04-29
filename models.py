from django.db import models
from django.urls import reverse
# Create your models here.
class Beer(models.Model):
    Bname=models.CharField(max_length=20)
    Taste=models.CharField(max_length=15)
    color=models.CharField(max_length=10)
    price=models.IntegerField()

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.id})