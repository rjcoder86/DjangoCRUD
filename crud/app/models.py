from django.db import models

class employees(models.Model):
    empid=models.AutoField(primary_key=True, auto_created=True)
    name=models.CharField(max_length=30)
    salary=models.IntegerField()
    # deptid=models.OneToOneField(department,on_delete=models.CASCADE)

