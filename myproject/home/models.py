from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=50, blank=True, default="")   # ye line add karo

    def __str__(self):
        return self.name