from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(blank=True)
    description = models.TextField()
    image = models.ImageField(default='blank.png',blank=True)



def __str__(self):
    return self.name+"-"+self.description