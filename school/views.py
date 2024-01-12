from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, filters, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import  cache_page

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

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            course_id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + course_id
            return response

        return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @method_decorator(cache_page(60))
    def dispatch(self, request, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(request, *args, **kwargs)


class ListRegistrationsByStudentView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs['pk'])

    serializer_class = ListRegistrationsByStudentSerializer


class ListStudentsByCourseView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(course_id=self.kwargs['pk'])

    serializer_class = ListStudentsByCourseSerializer
