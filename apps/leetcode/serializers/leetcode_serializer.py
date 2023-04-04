from rest_framework import serializers
from apps.leetcode.models.leet_code_problem import LeetCodeProblem


class LeetCodeProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = LeetCodeProblem
        fields = '__all__'
