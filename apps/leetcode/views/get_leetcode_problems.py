from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status
from django.core.cache import cache
from apps.leetcode.managers.leetcode_manager import LeetCodeManager
from apps.leetcode.serializers.leetcode_serializer import LeetCodeProblemSerializer


class LeetCodeProblemsView(APIView):
    
    def __init__(self):
        self.leet_manager = LeetCodeManager()

    def get(self,request):
        try:
            cache_key = "leetcode_problems"
            if cache.get(cache_key):
                return Response(cache.get(cache_key),status=status.HTTP_200_OK)
            limit = request.GET.get('limit')
            if limit:
                problems = self.leet_manager.get_problems(limit=limit)  
                data = LeetCodeProblemSerializer(problems,many=True).data
                cache.set(cache_key,data,7200)
                return Response(data,status=status.HTTP_200_OK)
            problems = self.leet_manager.get_problems()
            data = LeetCodeProblemSerializer(problems,many=True).data
            return render(request,'leetcode_problems.html',context={'problems':data})
            return Response(data=data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"queryset":str(problems),"error":str(e)},status=status.HTTP_400_BAD_REQUEST)