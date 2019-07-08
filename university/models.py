from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class University(models.Model):
    Choices = [
        ('gov', 'Governmental'),
        ('ngo', 'non-governmental'),
    ]
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    type = models.CharField(max_length=100, choices=Choices, default='gov')

    def __str__(self):
        return self.name


class Faculty(models.Model):
    class Meta:
        ordering = ('title',)

    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        ordering = ('title',)

    Choices = [(0, 'active'), (1, 'inactive')]
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    term = models.IntegerField(choices=Choices, default=0)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    class Meta:
        ordering = ('last_name',)

    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    # user = models.OneToOneField(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )

    def __str___(self):
        return self.last_name


class StudentCard(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    code_hex = models.CharField(max_length=100)
    code_digit = models.CharField(max_length=100)
    Choices = [('yes', 'yes'), ('no', 'no')]
    in_use = models.CharField(max_length=10, choices=Choices, default='yes')

    def __str__(self):
        return self.code_digit


class Student(models.Model):
    Choices = [
        ('active', 'active'),
        ('inactivate', 'inactivate'),
    ]

    id = models.PositiveIntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    entrance = models.IntegerField()
    activate_type = models.CharField(max_length=100, choices=Choices, default='active')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    studentCard = models.OneToOneField(StudentCard, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
