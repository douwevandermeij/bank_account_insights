from django.db import models


# Create your models here.
class Rekening(models.Model):
    nr = models.CharField(max_length=255)
    naam_omschrijving = models.CharField(max_length=255)


class Boeking(models.Model):
    datum = models.DateField()
    tegenrekening = models.ForeignKey(Rekening)
    code = models.CharField(max_length=2)
    af = models.BooleanField()
    bedrag = models.FloatField()
    mutatiesoort = models.CharField(max_length=25)
    mededelingen = models.CharField(max_length=255)
