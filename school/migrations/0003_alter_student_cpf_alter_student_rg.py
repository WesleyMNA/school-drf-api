# Generated by Django 5.0.1 on 2024-01-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='rg',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
