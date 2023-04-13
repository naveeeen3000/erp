from django.urls import path 
from apps.leetcode.views.get_leetcode_problems import LeetCodeProblemsView
from apps.leetcode.views.update_problem import UpdateLeetCodeProblemView
urlpatterns = [
    path('problems',LeetCodeProblemsView.as_view(),name='leetcode_problems'),
    path('problem/<int:id>',UpdateLeetCodeProblemView.as_view(),name='update-problem'),
]
