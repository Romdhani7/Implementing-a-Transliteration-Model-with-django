from enum import auto
from django.db import models
from django.db import connections


# Create your models here.

class Trans (models.Model):
    id = models.IntegerField(primary_key=True)
    Noun=models.CharField(max_length=100)
    Datebirth=models.DateField()
    Adress=models.CharField(max_length=100, blank=True, default="ABCD")
    Nationality=models.CharField(max_length=100)
    Place_of_birth=models.CharField(max_length=100, blank=True, default="")
    class Meta :
         db_table='dataset'

    def __str__(self):
        return self.Noun
    