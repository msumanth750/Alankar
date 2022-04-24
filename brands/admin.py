from django.contrib import admin
from .models import Brand
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Brand)
class ViewAdmin(ImportExportModelAdmin):
    list_display =['name','ncode','scode']

# Register your models here.
