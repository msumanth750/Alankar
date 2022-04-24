from django.contrib import admin
from .models import Exp
# Register your models here.
class ExpAdmin(admin.ModelAdmin):
    list_display = ['cdate','name','amount']

admin.site.register(Exp,ExpAdmin)
