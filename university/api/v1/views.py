from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from university.models import University, Student, StudentCard, Teacher, Course, Faculty
from university.api.v1.serializers import UniversitySerializer, StudentSerializer, StudentCardSerializer, TeacherSerializer, FacultySerializer, CourseSerializer

from jwt import decode

class StudentView(APIView):
    def get(self, request):
        # student = Student.objects.all()
        user = request.user
        student_list = []
        if hasattr(user, 'student') == True:
            student_list.append(user.student)
        elif hasattr(user, 'teacher') == True:
            courses = user.teacher.courses.all()
            for course in courses : 
                students = course.student_set.all()
                for student in students :
                    student_list.append(student)
        student_list = list(set(student_list))
        # student = request.user.student
        serializer = StudentSerializer(student_list, many=True)
        return Response({   
            "students": serializer.data,
                    
        })

    def post(self, request):
        student = request.data.get('student')
        serializer = StudentSerializer(data=student)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # user = User.objects.create_user()
            
        return Response({
            "success": "Student '{}' created successfully".format(student)}
        )


class StudentCardView(APIView):
    def get(self, request):
        
        # studentCard = StudentCard.objects.all()
        studentCard = request.user.student.studentCard
        serializer = StudentCardSerializer(studentCard)
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
        # teacher = Teacher.objects.all()
        user = request.user
        all_teacher = []
        if hasattr(user, 'teacher') == True:
            all_teacher.append(user.teacher)
        elif hasattr(user, 'student') == True:
            courses = user.student.courses.all()
            for course in courses :
                teachers = course.teacher_set.all()
                for teacher in teachers:
                    all_teacher.append(teacher)

        all_teacher = list(set(all_teacher))
        # teacher = Teacher.objects.get(pk=id)
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
        if hasattr(user, 'teacher') == True :
            course = user.teacher.courses
        elif hasattr(user, 'student') == True :
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
        if hasattr(user, 'teacher') == True :
            faculty = user.teacher.faculty
        elif hasattr(user, 'student') == True :
            faculty = user.student.faculty
        university = faculty.university
        # university = University.objects.all()
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
            {"success": "university '{}' created successfully".format(university)}
        )

class FacultyView(APIView):
    def get(self, request):
        user = request.user
        if hasattr(user, 'teacher') == True :
            faculty = user.teacher.faculty
        elif hasattr(user, 'student') == True :
            faculty = user.student.faculty
        # faculty = Faculty.objects.all()
        serializer = FacultySerializer(faculty)
        return Response(
            {"faculty": serializer.data}
        )
    def post(self, request):
        faculty = request.data.get('faculty')
        serializer = FacultySerializer(data=faculty)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "success": "faculty '{}' created successfully".format(faculty)
        })
