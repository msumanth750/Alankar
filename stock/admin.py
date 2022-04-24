from django.contrib import admin
from .models import Brand,Stock,Receits
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Stock)
class ViewAdmin(ImportExportModelAdmin):
    list_display =['date','brand','obal']
    list_filter =['date','brand']
    search_fields =['date']

@admin.register(Receits)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ['date','brand','qty']
    list_filter =['date','brand']
    search_fields =['date']


# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ['ncode','scode','name','type','qty','price',]
    list_filter = ['id']
admin.site.register(Brand,BrandAdmin)

'''class StockAdmin(admin.ModelAdmin):
    """docstring for StockAdmin."""
    list_display = ['date','brand','obal']
admin.site.register(Stock,StockAdmin)'''

'''class ReceitsAdmin(admin.ModelAdmin):
    list_display = ['date','brand','qty']
admin.site.register(Receits,ReceitsAdmin)'''
