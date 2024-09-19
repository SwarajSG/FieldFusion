from django.db import models
from mongoengine import Document, StringField, IntField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class User(Document):
    name = StringField(max_length=50)
    age = IntField() 

class Crop_Recommendation(models.Model):
    Nitrogen = IntField()
    Phosphorus = IntField()
    Potassium = IntField()
    temperature = float()
    humidity = float()
    ph = float()
    rainfall = float()
    label = StringField()

def __str__(self):
        return self.name