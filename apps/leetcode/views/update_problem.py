from apps.leetcode.managers.leetcode_manager import LeetCodeManager
from apps.leetcode.serializers.leetcode_serializer import LeetCodeProblemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UpdateLeetCodeProblemView(APIView):



    def __init__(self):
        self.leet_manager = LeetCodeManager()

    def get(self,request,id):
        problem = self.leet_manager.get_probelm_by_id(id)
        if not problem:
            return Response({'error':'not found'},status=status.HTTP_404_NOT_FOUND)
        data = LeetCodeProblemSerializer(problem,many=True).data
        return Response({'data':data},status=status.HTTP_200_OK)


    def post(self,request,id):
        # try:
        body = request.data
        print(body)
        if 'fields' in body :
            fields_to_update = body['fields']
        updated = self.leet_manager.update_problem(id,**fields_to_update)
        if updated: 
            return Response({'status':'success'},status=status.HTTP_200_OK)
        return Response({"status":"failed"},status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     from traceback import format_exc
        #     return Response({'status':'failed','error':str(format_exc())},status=status.HTTP_400_BAD_REQUEST)
        
