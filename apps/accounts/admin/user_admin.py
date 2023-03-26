from django.contrib import admin
from apps.accounts.models.users import Users
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    list_display = ['student_id','first_name','last_name','email','profile_image']

    fieldsets = (
        ("Personal Info",{
            'fields': ('student_id','profile_image','username','first_name','last_name',
                        'role','summary','address')
        }),
    )

    add_fieldsets = (
        (None,{
            "fields": ('student_id','username','password1','password2')
        }),
        ("Personale Info",{
            'fields': ("first_name",'last_name','role','email')
        })
    )

admin.site.register(Users,CustomUserAdmin)