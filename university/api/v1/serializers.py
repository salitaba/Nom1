from rest_framework import serializers
from university.models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    def create(self, validated_data):
        return Course.objects.create(**validated_data)



class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
    def create(self, validated_data):
        return Faculty.objects.create(**validated_data)
    
class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCard
        fields = '__all__'
    def create(self, validated_data):
        return StudentCard.objects.create(**validated_data)


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        course_data = validated_data.pop('courses')
        student = Student.objects.create(**validated_data)
        for course in course_data :
            student.courses.add(course)
        return student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        course_data = validated_data.pop('courses')
        teacher = Teacher.objects.create(**validated_data)
        for course in course_data :
            teacher.courses.add(course)
        return teacher




class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


