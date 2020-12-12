from django.contrib import admin

# Register your models here.
from Operations.models import Customer,Account

admin.site.register(Customer)
admin.site.register(Account)
