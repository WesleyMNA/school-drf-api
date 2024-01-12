import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from school.models import Student, Course


def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(
            random.randrange(10, 99),
            random.randrange(100, 999),
            random.randrange(100, 999),
            random.randrange(0, 9)
        )
        cpf = cpf.generate()
        birthday = fake.date_between(start_date='-18y', end_date='today')
        a = Student(name=name, rg=rg, cpf=cpf, birthday=birthday)
        a.save()


def criando_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        code = "{}{}-{}".format(
            random.choice("ABCDEF"),
            random.randrange(10, 99),
            random.randrange(1, 9)
        )
        descriptions = [
            'Python Fundamentos',
            'Python intermediário',
            'Python Avançado',
            'Python para Data Science',
            'Python/React'
        ]
        description = random.choice(descriptions)
        descriptions.remove(description)
        level = random.choice("BIA")
        c = Course(code=code, description=description, level=level)
        c.save()


criando_alunos(200)
criando_cursos(5)
