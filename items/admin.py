from django.contrib import admin

from items.models import CompanyBrand, CompanyItem, BranchItem

admin.site.register(CompanyBrand)
admin.site.register(CompanyItem)
admin.site.register(BranchItem)
