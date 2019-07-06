from django.db import models

# Create your models here.

class University (models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=10)
    Choices = [('gov', 'Governmental'), ('ngo', 'non-governmental')]
    type = models.CharField(max_length=100, choices=Choices, default='gov')
    def __str__(self):
        return self.name

class Faculty(models.Model):
    id = models.IntegerField
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

    university = models.ForeignKey(University, on_delete=models.CASCADE)

class Course(models.Model):
    class Meta:
        ordering = ('title',)

    id = models.IntegerField
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    start = models.DateTimeField
    end = models.DateTimeField
    Choices = [('active', 'active'), ('inactive', 'inactive')]
    term = models.CharField(max_length=10, choices=Choices, default='activate')

    def __str__(self):
        return self.title

class Teacher (models.Model):
    class Meta:
        ordering = ('last_name',)
    id = models.IntegerField
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    courses = models.ManyToManyField(Course)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str___(self):
        return self.last_name



class StudentCard (models.Model):
    id = models.IntegerField
    code_hex = models.CharField(max_length=100)
    code_digit = models.CharField(max_length=100)
    Choices = [('yes', 'yes'), ('no', 'no')]
    in_use = models.CharField(max_length=10, choices=Choices, default='yes')

    def __str__(self):
        return self.code_digit

class Student (models.Model):
    id = models.IntegerField
    code = models.CharField(max_length=100)
    entrance = models.IntegerField()
    Choices = [('active', 'active'), ('inactivate', 'inactivate')]
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

