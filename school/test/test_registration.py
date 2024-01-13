from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Registration, Course, Student


class RegistrationTest(APITestCase):

    def setUp(self):
        self.list_url = reverse('Registrations-list')
        self.course1 = Course.objects.create(code='TC1', description='Test Course 1', level='B')
        self.course2 = Course.objects.create(code='TC2', description='Test Course 2', level='A')
        self.student1 = Student.objects.create(
            name='Student 1',
            rg='123456789',
            cpf='12345678901',
            birthday='2024-01-01',
            phone_number='00911223344'
        )
        self.student2 = Student.objects.create(
            name='Student 2',
            rg='987654321',
            cpf='98765432109',
            birthday='2024-01-01',
            phone_number='99188776655'
        )
        self.registration1 = Registration.objects.create(student=self.student1, course=self.course1, period='M')
        self.registration2 = Registration.objects.create(student=self.student2, course=self.course2, period='M')

    def tearDown(self):
        Student.objects.all().delete()
        Course.objects.all().delete()
        Registration.objects.all().delete()

    def test_delete_not_allowed(self):
        response = self.client.delete(f'/registrations/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
