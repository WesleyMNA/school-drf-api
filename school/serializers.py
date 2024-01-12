from rest_framework import serializers

from .models import Student, Course, Registration
from .validators import name_is_invalid, cpf_is_invalid, rg_is_invalid


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'rg', 'cpf', 'birthday')

    def validate(self, attrs):
        errors = {}

        if name_is_invalid(attrs['name']):
            errors['name'] = 'name must only have letters'
        if cpf_is_invalid(attrs['cpf']):
            errors['cpf'] = 'cpf must have 11 digits'
        if rg_is_invalid(attrs['rg']):
            errors['rg'] = 'rg must have 9 digits'

        if errors:
            raise serializers.ValidationError(errors)

        return attrs


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
