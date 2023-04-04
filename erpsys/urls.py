from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leetcode/',include("apps.leetcode"),name='leetcode'),
]
