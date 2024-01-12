from rest_framework import viewsets, generics
from .models import Student, Course, Registration
from .serializers import StudentSerializer, CourseSerializer, RegistrationSerializer, ListRegistrationByStudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class ListRegistrationByStudentView(generics.ListAPIView):
    def get_queryset(self):
        return Registration.objects.filter(student_id=self.kwargs['pk'])

    serializer_class = ListRegistrationByStudentSerializer
