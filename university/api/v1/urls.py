from django.urls import path

from university.api.v1.views import StudentView, StudentCardView, TeacherView, CourseView, UniversityView, FacultyView, InfoView, CourseStudents, CourseTeachers

app_name = "university"

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('info/', InfoView.as_view()),
    path('courses/<int:id>/students/', CourseStudents.as_view()),
    path('courses/<int:id>/teachers/', CourseTeachers.as_view()),
    path('student_cards/', StudentCardView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('courses/', CourseView.as_view()),
    path('universities/', UniversityView.as_view()),
    path('faculties/', FacultyView.as_view()),
]

