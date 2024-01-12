from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters

from .models import Student, Course, Registration
from .serializers import (
    StudentSerializer,
    StudentSerializerV2,
    CourseSerializer,
    RegistrationSerializer,
    ListRegistrationsByStudentSerializer,
    ListStudentsByCourseSerializer
)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return StudentSerializerV2
        return StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['code', 'description']
    search_fields = ['code']


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class ListRegistrationsByStudentView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs['pk'])

    serializer_class = ListRegistrationsByStudentSerializer


class ListStudentsByCourseView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])

    serializer_class = ListStudentsByCourseSerializer
