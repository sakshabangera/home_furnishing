# Generated by Django 4.1.13 on 2024-02-09 04:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=100, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
