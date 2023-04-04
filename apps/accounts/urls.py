from django.urls import path
from apps.accounts.views.users_view import UserView

urlpatterns = [
    path('user/',UserView.as_view(),name='user-view'),
]