# Generated by Django 4.0.3 on 2022-04-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='deptid',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employees',
            name='empid',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
