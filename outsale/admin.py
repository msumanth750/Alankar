from django.contrib import admin
from .models import Outsale

# Register your models here.
class OutsaleAdmin(admin.ModelAdmin):
    """docstring for OutsaleAdmin."""
    list_display =['brand','date','qty']
admin.site.register(Outsale,OutsaleAdmin)
