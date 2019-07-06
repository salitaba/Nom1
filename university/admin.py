from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Teacher)
admin.site.register(StudentCard)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(University)
admin.site.register(Course)