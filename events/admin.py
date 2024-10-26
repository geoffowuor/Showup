from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display =('name','description', 'day_date', 'time', 'venue')
    search_fields = ('name','venue')
    filter = ('name', 'day_date', 'venue')