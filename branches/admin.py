from django.contrib import admin
from branches.models import Company, Branch, BranchUser


class CompanyAdmin(admin.ModelAdmin):
    model = Company


class BranchAdmin(admin.ModelAdmin):
    model = Branch


admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(BranchUser)
