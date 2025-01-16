from django.db import models

class Person(models.Model):
    objects = None

    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    area_code = models.CharField(max_length=5)
    exist = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.last_name},{self.first_name}"
