from django.contrib import admin
from django.urls import path

from Operations.views import AccountAPI, CustomerAPI, GetAccountBalanceAPI

urlpatterns = [
    path('account-api/', AccountAPI.as_view()),
    path('customer-api/', CustomerAPI.as_view()),
    path('balance-api/', GetAccountBalanceAPI.as_view()),

]
