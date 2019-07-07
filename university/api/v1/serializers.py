from rest_framework import serializers
from university.models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'
    
class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCard
        fields = '__all__'



class StudentSerializer(serializers.ModelSerializer):
    # courses = CourseSerializer(many=True)
    # faculty = FacultySerializer()
    # studentCard = StudentCardSerializer()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        course_data = validated_data.pop('courses')
        # studentCard = validated_data.pop('studentCard')
        student = Student.objects.create(**validated_data)
        # student.studentCard.add(studentCard)
        for id in course_data :
            student.courses.add(id)
        return student
        # return Student.objects.create(**validated_data)


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'




class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


