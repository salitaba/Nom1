from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from university.models import University, Student, StudentCard, Teacher, Course, Faculty
from university.api.v1.serializers import UniversitySerializer, StudentSerializer, StudentCardSerializer, TeacherSerializer, FacultySerializer, UniversitySerializer


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
            serializer.save()
            # user = User.objects.create_user()
            
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
    def post(self, request):
        student_card = request.data.get('student_card')
        serializer = StudentCardSerializer(data=student_card)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "Student_card '{}' created successfully".format(student_card)}
        )


class TeacherView(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(
            {"teachers": serializer.data}
        )
    def post(self, request):
        teacher = request.data.get('teacher')
        serializer = TeacherSerializer(data=teacher)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "teacher '{}' created successfully".format(teacher)}
        )
    


class CourseView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(
            {"courses": serializer.data}
        )
    def post(self, request):
        course = request.data.get('course')
        serializer = CourseSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "course '{}' created successfully".format(course)}
        )


class UniversityView(APIView):
    def get(self, request):
        university = University.objects.all()
        serializer = UniversitySerializer(university, many=True)
        return Response(
            {"university": serializer.data}
        )
    def post(self, request):
        university = request.data.get('university')
        serializer = UniversitySerializer(data=university)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "university '{}' created successfully".format(university)}
        )

class FacultyView(APIView):
    def get(self, request):
        faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty, many=True)
        return Response(
            {"faculty": serializer.data}
        )
    def post(self, request):
        faculty = request.data.get('faculty')
        serializer = FacultySerializer(data=faculty)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "faculty '{}' created successfully".format(faculty)}
        )
