from django.urls import path

from university.api.v1.views import *

app_name = "university"

urlpatterns = [
    path('students/', StudentView.as_view()),
    path('student_cards/', StudentCardView.as_view()),
    path('teachers/', TeacherView.as_view()),
    path('courses/', CourseView.as_view()),
    path('universities/', UniversityView.as_view()),
    path('faculties/', FacultyView.as_view()),
]

