from rest_framework.response import Response
from rest_framework.views import APIView

from university.models import *
from university.api.v1.serializers import *


class StudentView(APIView):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(
            {"students": serializer.data}
        )


class StudentCardView(APIView):
    def get(self, request):
        studentCard = StudentCard.objects.all()
        serializer = StudentCardSerializer(studentCard, many=True)
        return Response(
            {"students": serializer.data}
        )


class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(
            {"students": serializer.data}
        )


