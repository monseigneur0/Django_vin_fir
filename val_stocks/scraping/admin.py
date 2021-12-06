from django.contrib import admin

# Register your models here.
# from .models import User ,Wine, manwine
#
# admin.site.register(User)
# # Register your models here.
# admin.site.register(Wine)
# admin.site.register(manwine)
from .models import Company
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']
# research function
admin.site.register(Company,CompanyAdmin)