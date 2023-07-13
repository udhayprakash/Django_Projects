"""
"""
from django.db import models

class Gender(models.Model):
    """ Gender db table"""
    name = models.CharField(max_length=50)

class Person(models.Model):
    """ Person db table"""
    SSN = models.CharField(max_length=512, null=True, blank=True)
    first_name = models.CharField(max_length=65, null=True, blank=True)
    last_name = models.CharField(max_length=65, null=True, blank=True)
    middle_name = models.CharField(max_length=65, null=True, blank=True)
    name_prefix_code = models.CharField(max_length=4, null=True, blank=True)
    name_suffix_code = models.CharField(max_length=4, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
