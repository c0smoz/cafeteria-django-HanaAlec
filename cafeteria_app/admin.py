from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

admin.site.register(Product)
admin.site.register(Transaction)

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    pass
