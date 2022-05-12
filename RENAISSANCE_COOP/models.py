from distutils.command.upload import upload
from unicodedata import name
from django.db import models

# Create your models here.

# la classe de produits
class Produit(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="pics")
    desc = models.TextField()
    price = models.IntegerField()
    user = models.TextField()

# classe pour les commentaires
class Comment(models.Model):
    description = models.TextField()
