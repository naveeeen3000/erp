from django.contrib import admin
from apps.core.models.institute_types import InstituteTypes


class InstituteTypeAdmin(admin.ModelAdmin):

    list_display = ['education','school_level']
    

admin.site.register(InstituteTypes,InstituteTypeAdmin)