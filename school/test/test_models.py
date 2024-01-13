from django.db import IntegrityError
from django.test import TestCase
from ..models import Student


class StudentTest(TestCase):

    def setUp(self):
        self.student = Student.objects.create(
            name='Student 1',
            rg='123456789',
            cpf='12345678901',
            birthday='2024-01-01',
            phone_number='00911223344'
        )

    def test_student_with_unique_fields(self):
        with self.assertRaises(IntegrityError):
            Student.objects.create(
                name='Student 2',
                rg=self.student.rg,
                cpf=self.student.cpf,
                birthday=self.student.birthday,
                phone_number=self.student.phone_number,
            )
