from django.db import models

# Create your models here.
class List(models.Model):
    image = models.ImageField(upload_to='images')  
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name