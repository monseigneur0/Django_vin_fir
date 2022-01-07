from django.contrib import admin

# Register your models here.
# from .models import User ,Wine, manwine
#
# admin.site.register(User)
# # Register your models here.
# admin.site.register(Wine)
# admin.site.register(manwine)
from .models import Company, Category, Quarter, Daily
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']
# research function
admin.site.register(Company,CompanyAdmin)

class CompanyAdmin1(admin.ModelAdmin):
    search_fields = ['Category']
# research function
admin.site.register(Category,CompanyAdmin1)

class CompanyAdmin2(admin.ModelAdmin):
    search_fields = ['Quarter']
# research function
admin.site.register(Quarter,CompanyAdmin2)

class CompanyAdmin3(admin.ModelAdmin):
    search_fields = ['Daily']
# research function
admin.site.register(Daily,CompanyAdmin3)