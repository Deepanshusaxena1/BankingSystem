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

class Account(models.Model):
    account_type_choices = (
        ("savings", "savings"),
        ("salary", "salary"),
        ("loan", "loan"),
        ("current", "current"),
    )
    account_number = models.CharField(max_length=15, unique=True)
    account_holder = models.OneToOneField(Customer, on_delete=models.CASCADE)
    current_amount = models.FloatField(default=0)
    account_type = models.CharField(choices=account_type_choices, max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_number

