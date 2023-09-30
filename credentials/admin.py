from django.contrib import admin
from .models import Student, Courses, Department

# Register your models here.

admin.site.register(Student)
admin.site.register(Courses)
admin.site.register(Department)
