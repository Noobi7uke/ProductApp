from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    quantity = models.IntegerField(default=0)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.name