# Generated by Django 4.0.3 on 2022-05-26 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_employees_deptid_department_emp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='department',
        ),
    ]