from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Course


class CourseTest(APITestCase):

    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course1 = Course.objects.create(code='TC1', description='Test Course 1', level='B')
        self.course2 = Course.objects.create(code='TC2', description='Test Course 2', level='A')

    def tearDown(self):
        User.objects.all().delete()
        Course.objects.all().delete()

    def test_get_all_courses(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        data = {'code': 'TC3', 'description': 'Test Course 3', 'level': 'I'}
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_update_course(self):
        data = {'code': 'TC1', 'description': 'Course updated', 'level': 'I'}
        response = self.client.put('/courses/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
