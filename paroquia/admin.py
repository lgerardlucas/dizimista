from django.contrib import admin
from .models import Paroquia

class ParoquiaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_diplay_links = ('name',)
    
admin.site.register(Paroquia,ParoquiaAdmin)
