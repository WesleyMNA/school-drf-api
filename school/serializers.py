from rest_framework import serializers

from .models import Student, Course, Registration


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'rg', 'cpf', 'birthday')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []


class ListRegistrationsByStudentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, registration):
        return registration.get_period_display()


class ListStudentsByCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')

    class Meta:
        model = Registration
        fields = ['student_name']
