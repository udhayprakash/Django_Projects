from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomerDetails(models.Model):
    """
    Stores the information about all the customers
    """
    name = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30)
    telephone_number = PhoneNumberField()
    date_of_contact = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
