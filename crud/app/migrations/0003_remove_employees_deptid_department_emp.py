# Generated by Django 4.0.3 on 2022-04-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_department_deptid_alter_employees_empid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='deptid',
        ),
        migrations.AddField(
            model_name='department',
            name='emp',
            field=models.ManyToManyField(to='app.employees'),
        ),
    ]
