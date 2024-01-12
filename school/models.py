from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    rg = models.CharField(max_length=9, unique=True, null=False, blank=False)
    cpf = models.CharField(max_length=11, unique=True, null=False, blank=False)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11, unique=True, null=True)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVELS = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced'),
    )

    code = models.CharField(max_length=10, unique=True, null=False)
    description = models.CharField(max_length=100, null=False)
    level = models.CharField(max_length=1, choices=LEVELS, blank=False, null=False, default='B')

    def __str__(self):
        return self.description


class Registration(models.Model):
    PERIODS = (
        ('M', 'Morning'),
        ('A', 'Afternoon'),
        ('N', 'Night'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    period = models.CharField(max_length=1, choices=PERIODS, blank=False, null=False, default='M')

    def __str__(self):
        return f'{self.student.name} - {self.course.code} - {self.period}'
