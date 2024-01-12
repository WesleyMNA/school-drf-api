from django.urls import path, include
from rest_framework import routers

from .views import StudentViewSet, CourseViewSet

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')

urlpatterns = [
    path('', include(router.urls))
]
