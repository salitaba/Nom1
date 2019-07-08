from django.shortcuts import render

from university.api.v1.views import Teacher
from university.api.v1.serializers import TeacherSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from jwt import decode
# Create your views here.

class hello_world(APIView):
    def get(self, request):
        # token = request.META.get('HTTP_ID')
        teacher = request.user.teacher.last_name
        return Response({
            # 'REAL_ID' : token,
            # 'user_id' : decode(token),
            'username' : teacher,
            "id": "id",
        })