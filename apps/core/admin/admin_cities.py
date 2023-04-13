from django.contrib import admin
from apps.core.models.cities import Cities


class CitiesAdmin(admin.ModelAdmin):
    list_display = ['name','state','created_by']
    readonly_fields = ['state','created_at','created_by']
    

admin.site.register(Cities,CitiesAdmin)