from django.urls import path, include
from rest_framework import routers

from .views import StudentViewSet, CourseViewSet, RegistrationViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('', include(router.urls))
]
