from distutils.command.upload import upload
from django.db import models

# Create your models here.

class Produit(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    price = models.IntegerField()