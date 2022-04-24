from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Loan

# Register your models here.
@admin.register(Loan)
class LoanAdmin(ImportExportModelAdmin):
    list_display = ['tdate','name','amount']
