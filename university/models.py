from django.contrib.auth import get_user_model
from django.db import models


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

    university = models.ForeignKey(
        to=University,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Course(models.Model):
    class Meta:
        ordering = ('title',)

    course_active_choices = [
        (0, 'inactive'),
        (1, 'active'),
    ]

    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    course_status_type = models.IntegerField(choices=course_active_choices, default=0)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    class Meta:
        ordering = ('last_name',)

    id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    courses = models.ManyToManyField(
        to=Course,
        blank=True,
    )
    faculty = models.ForeignKey(
        to=Faculty,
        on_delete=models.CASCADE,
    )
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        default=None,
    )

    def __str___(self):
        return self.last_name


class StudentCard(models.Model):
    inuse_choices = [
        (0, 'not inuse'),
        (1, 'inuse'),
        (9, 'Expired'),
    ]

    id = models.PositiveIntegerField(primary_key=True)
    code_hex = models.CharField(max_length=100)
    code_digit = models.CharField(max_length=100)
    in_use_status = models.IntegerField(choices=inuse_choices, default=inuse_choices[0][0])

    def __str__(self):
        return self.code_digit


class Student(models.Model):
    student_active_choices = [
        (0, 'inactive'),
        (1, 'active'),
        (2, 'blocked'),
        (9, 'banned'),
    ]

    id = models.PositiveIntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    entrance = models.IntegerField()
    active_status_type = models.CharField(max_length=100, choices=student_active_choices,
                                          default=student_active_choices[0][0])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    courses = models.ManyToManyField(
        to=Course,
        blank=True,
    )
    faculty = models.ForeignKey(
        to=Faculty,
        on_delete=models.CASCADE,
    )
    studentCard = models.OneToOneField(
        to=StudentCard,
        on_delete=models.CASCADE,
    )
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
