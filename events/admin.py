from django.contrib import admin
from .models import Event

# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display =('name','description', 'date')
    search_fields = ('name','date')
    filter = ('name', 'date')