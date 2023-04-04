from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.leetcode.managers.leetcode_manager import LeetCodeManager
from apps.leetcode.serializers.leetcode_serializer import LeetCodeProblemSerializer


class LeetCodeProblemsView(APIView):
    
    def __init__(self):
        self.leet_manager = LeetCodeManager()

    def get(self,request):
        try:
            problems = self.leet_manager.get_problems()
            data = LeetCodeProblemSerializer(problems).data

            return Response(data=data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)