from rest_framework.views import APIView
from rest_framework.response import Response


class UserView(APIView):


    def __init__(self):
        pass

    def get(self,request):
        return Response("something")