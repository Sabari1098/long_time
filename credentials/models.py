from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'credentials_department'

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'credentials_courses'


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    age = models.CharField(max_length=25)
    gender = models.CharField(max_length=15)
    phone = models.TextField(max_length=20)
    mail = models.EmailField()
    address = models.TextField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Courses, on_delete=models.SET_NULL, null=True)
    purpose = models.TextField(max_length=50, null=True)
    material = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'credentials_student'
