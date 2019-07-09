from rest_framework.response import Response
from rest_framework.views import APIView
# from django.contrib.auth.models import User

from university.models import University, Student, StudentCard, Teacher, Course, Faculty
from university.api.v1.serializers import UniversitySerializer, StudentSerializer, StudentCardSerializer, TeacherSerializer, FacultySerializer, CourseSerializer

# from jwt import decode

YOU_ARE_NOT_ADMIN = {"Authencation" : "you are not super user"}
PERMISSION_ERROR = { "Permissoin" : "denied" }

class StudentView(APIView):
    def get(self, request):
        # student = Student.objects.all()
        user = request.user
        if user.is_superuser is False:
            return Response(YOU_ARE_NOT_ADMIN)
        # student_list = []
        # if hasattr(user, 'student') == True:
        #     student_list.append(user.student)
        # elif hasattr(user, 'teacher') == True:
        #     courses = user.teacher.courses.all()
        #     for course in courses:
        #         students = course.student_set.all()
        #         for student in students:
        #             student_list.append(student)
        # student_list = list(set(student_list))
        student_list = Student.objects.all()
        serializer = StudentSerializer(student_list, many=True)
        response = {
            "students": serializer.data,
        }
        return Response(response)

    def post(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        success = {
            "success": "Student '{}' created successfully".format(student)
        }
        return Response(success)


class StudentCardView(APIView):
    def get(self, request):
        if request.user.is_superuser is False:
            return Response(YOU_ARE_NOT_ADMIN)
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
            {"success": "Student_card '{}' created successfully".format(
                student_card)}
        )


class TeacherView(APIView):
    def get(self, request):
        # teacher = Teacher.objects.all()
        user = request.user
        if user.is_superuser is False:
            return Response(YOU_ARE_NOT_ADMIN)
        # all_teacher = []
        # if hasattr(user, 'teacher') == True:
        #     all_teacher.append(user.teacher)
        # elif hasattr(user, 'student') == True:
        #     courses = user.student.courses.all()
        #     for course in courses:
        #         teachers = course.teacher_set.all()
        #         for teacher in teachers:
        #             all_teacher.append(teacher)

        # all_teacher = list(set(all_teacher))
        all_teacher = Teacher.objects.all()
        serializer = TeacherSerializer(all_teacher, many=True)
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
        user = request.user
        if user.is_superuser is True : 
            course = Course.objects.all()
        if hasattr(user, 'teacher') == True:
            course = user.teacher.courses
        elif hasattr(user, 'student') == True:
            course = user.student.courses
        # course = Course.objects.all()
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
        user = request.user

        if user.is_superuser is True:
            university = University.objects.all()
            serializer = UniversitySerializer(university, many=True)
        if hasattr(user, 'teacher') == True:
            faculty = user.teacher.faculty.university
            serializer = UniversitySerializer(university)
        elif hasattr(user, 'student') == True:
            faculty = user.student.faculty.university
            serializer = UniversitySerializer(university)

        return Response(
            {"university": serializer.data}
        )

    def post(self, request):
        university = request.data.get('university')
        serializer = UniversitySerializer(data=university)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(
            {"success": "university '{}' created successfully".format(
                university)}
        )


class FacultyView(APIView):
    def get(self, request):
        user = request.user

        if user.is_superuser == True:
            faculty = Faculty.objects.all()
            serializer = FacultySerializer(faculty, many=True)
        if hasattr(user, 'teacher') == True:
            faculty = user.teacher.faculty
            serializer = FacultySerializer(faculty)
        elif hasattr(user, 'student') == True:
            faculty = user.student.faculty
            serializer = FacultySerializer(faculty)

        # faculty = Faculty.objects.all()
        response = {"faculty": serializer.data}
        return Response(response)

    def post(self, request):
        faculty = request.data.get('faculty')
        serializer = FacultySerializer(data=faculty)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "success": "faculty '{}' created successfully".format(faculty)
        })


class InfoView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'teacher'):
            teacher = user.teacher
            teacher_serializer = TeacherSerializer(teacher)
            response = {
                "teacher" : teacher_serializer.data,
            }
        elif hasattr(user, 'student'):
            student = user.student
            student_serializer = StudentSerializer(student)
            card_serializer = StudentCardSerializer(student.studentCard)
            response = { 
                "student" : student_serializer.data,
                "stucent_card" :  card_serializer.data,
            }        
        return Response(response)


class CourseStudents(APIView):
    def get(self, request, id):
        user = request.user
        if hasattr(user, 'teacher') is False:
            return Response(PERMISSION_ERROR)
        teacher = user.teacher
        course = teacher.courses.get(pk=id)
        serializer = StudentSerializer(course.student_set.all(), many=True)
        response = {"students" : serializer.data}
        return Response(response)


class CourseTeachers(APIView):
    def get(self, request, id):
        user = request.user
        if hasattr(user, 'student') is False:
            return Response(PERMISSION_ERROR)
        student = user.student
        course = student.courses.get(pk=id)
        serializer = TeacherSerializer(course.teacher_set.all(), many=True)
        response = {"teachers" : serializer.data}
        return Response(response)