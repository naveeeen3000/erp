from django.contrib import admin
from django.urls import path,include
from erpsys.helpers.custom_task_helper_view import custom_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include("apps.accounts")),
    path('custom_task/',custom_task,name='custom-task')
]
