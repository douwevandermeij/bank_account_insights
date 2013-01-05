from django.db import models
from django.db.models import Sum, Q


class BoekingenManager(models.Manager):
    def get_query_set(self):
        return super(BoekingenManager, self).get_query_set().filter(author='Roald Dahl')


class Categorie(models.Model):
    class Meta:
        verbose_name_plural = "Categorieen"

    def __unicode__(self):
        return self.naam

    naam = models.CharField(max_length=255)

#    boekingen = BoekingenManager()

    def totaal(self):
        totals = [b.netto() for b in Boeking.objects.filter(
            Q(
                Q(categorie=None) & Q(tegenrekening__categorie=self)
            ) | Q(categorie=self)
        )]
        return sum(totals)


class Rekening(models.Model):
    class Meta:
        verbose_name_plural = "Rekeningen"

    def __unicode__(self):
        return "{0} - {1}".format(self.nr, self.naam_omschrijving)

    nr = models.CharField(max_length=255, blank=True)
    naam_omschrijving = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie, default=17)

    def totaal(self):
        totals = [b.netto() for b in Boeking.objects.filter(tegenrekening=self)]
        return sum(totals)


class Boeking(models.Model):
    class Meta:
        verbose_name_plural = "Boekingen"

    datum = models.DateField()
    tegenrekening = models.ForeignKey(Rekening)
    code = models.CharField(max_length=2)
    af = models.BooleanField()
    bedrag = models.FloatField()
    mutatiesoort = models.CharField(max_length=25)
    mededelingen = models.CharField(max_length=255, blank=True)
    categorie = models.ForeignKey(Categorie, null=True, blank=True)

    def netto(self):
        if self.af:
            return self.bedrag
        return -self.bedrag

    def cat(self):
        if self.categorie == None:
            return self.tegenrekening.categorie
        return self.categorie


class RawData(models.Model):
    datum = models.CharField(max_length=25)
    naam_omschrijving = models.CharField(max_length=255)
    rekening = models.CharField(max_length=25)
    tegenrekening = models.CharField(max_length=25)
    code = models.CharField(max_length=2)
    af_bij = models.CharField(max_length=3)
    bedrag = models.CharField(max_length=10)
    mutatiesoort = models.CharField(max_length=25)
    mededelingen = models.CharField(max_length=255)

    processed = models.BooleanField(default=False)
