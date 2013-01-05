from django.contrib import admin
from geldzaken.core.models import Rekening, Boeking, RawData, Categorie
from datetime import datetime


def process(modeladmin, request, queryset):
    for el in queryset:
        if el.processed:
            continue

        rek = Rekening.objects.filter(nr=el.tegenrekening)
        if len(rek):
            rek = rek[0]
        else:
            rek = Rekening()
            rek.nr = el.tegenrekening
            rek.naam_omschrijving = el.naam_omschrijving
            rek.save()

        b = Boeking()
        b.datum = datetime.strptime(el.datum, '%d-%m-%Y')
        b.tegenrekening = rek
        b.code = el.code
        b.af = el.af_bij == 'Af'
        b.bedrag = float(el.bedrag.replace(',', '.'))
        b.mutatiesoort = el.mutatiesoort
        b.mededelingen = el.mededelingen
        b.save()

        el.processed=True
        el.save()
process.short_description = "Process data"

def categorize(modeladmin, request, queryset):
    queryset.filter(mutatiesoort="Geldautomaat").update(categorie=2)
    queryset.filter(mededelingen__contains="polis").update(categorie=5)
    queryset.filter(mededelingen__contains="albert").update(categorie=13)
    queryset.filter(mededelingen__contains="klim").update(categorie=14)
    queryset.filter(mededelingen__contains="c1000").update(categorie=13)
    queryset.filter(mededelingen__contains="edah").update(categorie=13)
    queryset.filter(mededelingen__contains="aldi").update(categorie=13)
    queryset.filter(mededelingen__contains="lidl").update(categorie=13)
    queryset.filter(mededelingen__contains="plus").update(categorie=13)
    queryset.filter(mededelingen__contains="shell").update(categorie=3)
    queryset.filter(mededelingen__contains="esso").update(categorie=3)
    queryset.filter(mededelingen__contains="tinq").update(categorie=3)
    queryset.filter(mededelingen__contains="firezone").update(categorie=3)
    queryset.filter(mededelingen__contains='bremer').update(categorie=3)
categorize.short_description = "Categorize data"


class RekeningInline(admin.TabularInline):
    model = Rekening
    extra = 0


class BoekingInline(admin.TabularInline):
    model = Boeking
    extra = 0


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('naam', 'totaal', )
    inlines = [RekeningInline, BoekingInline]


class RekeningAdmin(admin.ModelAdmin):
    list_display = ('nr', 'naam_omschrijving', 'categorie', 'totaal', )
    inlines = [BoekingInline]
    search_fields = ['naam_omschrijving']


class BoekingAdmin(admin.ModelAdmin):
    list_display = ('datum', 'tegenrekening', 'cat', 'bedrag', 'af', )
    actions = [categorize]
    search_fields = ['datum']


class RawDataAdmin(admin.ModelAdmin):
    list_display = ('datum', 'naam_omschrijving', 'tegenrekening', 'bedrag', 'mededelingen', 'processed', )
    actions = [process]


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Rekening, RekeningAdmin)
admin.site.register(Boeking, BoekingAdmin)
admin.site.register(RawData, RawDataAdmin)
