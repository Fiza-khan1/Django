from django.db import models

class User(models.Model):
    studentName=models.CharField(max_length=20)
    teachername=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=10)
    rePassword=models.CharField(max_length=10)

    def __str__(self):
        return self.studentName

