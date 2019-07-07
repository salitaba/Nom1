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

    def post(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            student_saved = serializer.save()
        return Response(
            {"success": "Student '{}' created successfully".format(student)}
        )


class StudentCardView(APIView):
    def get(self, request):
        studentCard = StudentCard.objects.all()
        serializer = StudentCardSerializer(studentCard, many=True)
        return Response(
            {"student_cards": serializer.data}
        )


class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(
            {"teachers": serializer.data}
        )


class CourseView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(
            {"courses": serializer.data}
        )


class UniversityView(APIView):
    def get(self, request):
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(
            {"university": serializer.data}
        )


class FacultyView(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(
            {"faculty": serializer.data}
        )
