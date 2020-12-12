from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50, blank=True)
    customer_email = models.EmailField(unique=True, max_length=200)
    customer_phone_number = models.CharField(unique=True, max_length=13)
    customer_occupation = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + str(self.customer_first_name)

