from django.db import models

class Student(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)


    m1 = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    dbms = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    result = models.CharField(max_length=10, blank=True)
    attendance = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

