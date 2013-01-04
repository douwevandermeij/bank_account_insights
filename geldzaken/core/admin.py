from django.contrib import admin
from geldzaken.core.models import Rekening, Boeking


class RekeningAdmin(admin.ModelAdmin):
    list_display = ('nr', 'naam_omschrijving', )


class BoekingAdmin(admin.ModelAdmin):
    list_display = ('datum', 'tegenrekening', 'bedrag' )


admin.site.register(Rekening, RekeningAdmin)
admin.site.register(Boeking, BoekingAdmin)
