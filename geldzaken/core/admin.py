from django.contrib import admin
from geldzaken.core.models import Rekening, Boeking, RawData, Categorie, CategorizeFilter
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
    for cf in CategorizeFilter.objects.all():
        queryset.filter(**{cf.field: cf.value}).update(categorie=cf.categorie)
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
    search_fields = ['datum']


class CategorizeFilterAdmin(admin.ModelAdmin):
    list_display = ('field', 'value', 'categorie', )

admin.site.register(CategorizeFilter, CategorizeFilterAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Rekening, RekeningAdmin)
admin.site.register(Boeking, BoekingAdmin)
admin.site.register(RawData, RawDataAdmin)
