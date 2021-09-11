from django.contrib import admin
from .models import Comunidade

class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)

admin.site.register(Comunidade,ComunidadeAdmin)
