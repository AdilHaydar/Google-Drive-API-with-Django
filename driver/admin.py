from django.contrib import admin
from .models import Organization,OrganizationMember,Folder,DocumentPackage,Document
# Register your models here.

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

    class Meta:
        model = Organization
