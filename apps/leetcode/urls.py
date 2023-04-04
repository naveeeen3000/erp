from django.urls import path 
from apps.leetcode.views.get_leetcode_problems import LeetCodeProblemsView

urlpatterns = [
    path('/problems',LeetCodeProblemsView.as_view(),name='leetcode_problems'),
]
