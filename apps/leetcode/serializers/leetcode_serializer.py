from rest_framework import serializers
from apps.leetcode.models.leet_code_problem import LeetCodeProblem


class LeetCodeProblemSerializer(serializers.ModelSerializer):
    
    def __init__(self, instance=None, data=..., **kwargs):
        super().__init__(instance, data, **kwargs)

    class Meta:
        model = LeetCodeProblem
        fields = '__all__'
        # exclude = ['leetcode_question_link']
        

    