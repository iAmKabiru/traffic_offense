from django.contrib import admin
from .models import OffenceCategory, Offence

@admin.register(OffenceCategory)
class OffenceCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'offences')

@admin.register(Offence)
class Offence(admin.ModelAdmin):
    list_display = ('id', 'title', 'person_name', 'offence', 'location', 'treated', 'date', 'updated')
    list_filter = ('offence', 'treated')