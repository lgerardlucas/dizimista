from django.contrib import admin
from .models import Ofertante

class OfertanteAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(Ofertante,OfertanteAdmin)
