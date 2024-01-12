from rest_framework import viewsets, generics, filters
from .models import Student, Course, Registration
from .serializers import (
    StudentSerializer,
    CourseSerializer,
    RegistrationSerializer,
    ListRegistrationsByStudentSerializer,
    ListStudentsByCourseSerializer
)
from django_filters.rest_framework import DjangoFilterBackend


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['code', 'description']
    search_fields = ['code']


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationsByStudentView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs['pk'])

    serializer_class = ListRegistrationsByStudentSerializer


class ListStudentsByCourseView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])

    serializer_class = ListStudentsByCourseSerializer
