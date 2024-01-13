from django.test import TestCase

from ..models import Student
from ..serializers import StudentSerializer


class StudentSerializerTest(TestCase):

    def setUp(self):
        self.student = Student(
            name='Student 1',
            rg='123456789',
            cpf='12345678901',
            birthday='2024-01-01',
            phone_number='00911223344'
        )
        self.serializer = StudentSerializer(instance=self.student)

    def test_serialized_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'rg', 'cpf', 'birthday', 'photo'})

    def test_serialized_content(self):
        data = self.serializer.data
        self.assertEquals(data['name'], self.student.name)
        self.assertEquals(data['rg'], self.student.rg)
        self.assertEquals(data['cpf'], self.student.cpf)
        self.assertEquals(data['birthday'], self.student.birthday)
