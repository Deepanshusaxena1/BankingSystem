# Create your views here.
import json
from json import JSONDecodeError

from rest_framework import status
from rest_framework.views import APIView
from Operations.models import Customer, Account
from Operations.serializers import CustomerSerializer, AccountSerializer
from Operations.utils import generate_json_response


class CustomerAPI(APIView):

    def get(self, request):
        try:
            request_json = json.loads(request.body)
        except JSONDecodeError:
            return generate_json_response(False, {}, "Request body could not be parsed", status.HTTP_400_BAD_REQUEST)
        try:
            customer_id = request_json["customer_id"]
        except KeyError:
            return generate_json_response(False, {}, "customer_id is missing.", status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer, many=False)
            return generate_json_response(True, {"customer": serializer.data}, "Customer details fetched Successfully",
                                          status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return generate_json_response(False, {}, "No such customer found.", status.HTTP_404_NOT_FOUND)

        # return generate_json_response(False, {}, "Some error occurred", status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return generate_json_response(True, {"customer": serializer.data}, "Customer created Successfully.",
                                          status.HTTP_201_CREATED)
        else:
            return generate_json_response(False, {}, serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            request_json = json.loads(request.body)
        except JSONDecodeError:
            return generate_json_response(False, {}, "Request body could not be parsed", status.HTTP_400_BAD_REQUEST)
        try:
            customer_id = request_json["customer_id"]
        except KeyError:
            return generate_json_response(False, {}, "customer_id is missing.", status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer, many=False)
            customer.delete()
            return generate_json_response(True, {"customer": serializer.data}, "Customer details deleted Successfully",
                                          status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return generate_json_response(False, {}, "No such customer found.", status.HTTP_404_NOT_FOUND)


class AccountAPI(APIView):
    def get(self, request):
        try:
            request_json = json.loads(request.body)
        except JSONDecodeError:
            return generate_json_response(False, {}, "Request body could not be parsed", status.HTTP_400_BAD_REQUEST)
        try:
            account_number = request_json["account_number"]
        except KeyError:
            return generate_json_response(False, {}, "account_number is missing.", status.HTTP_400_BAD_REQUEST)

        try:
            account = Account.objects.get(account_number=account_number)
            serializer = AccountSerializer(account, many=False)
            return generate_json_response(True, {"account": serializer.data}, "Account details fetched Successfully",
                                          status.HTTP_200_OK)
        except Account.DoesNotExist:
            return generate_json_response(False, {}, "No such account found.", status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return generate_json_response(True, {"account": serializer.data}, "Account created Successfully.",
                                          status.HTTP_201_CREATED)
        else:
            return generate_json_response(False, {}, serializer.errors, status.HTTP_400_BAD_REQUEST)


class GetAccountBalanceAPI(APIView):
    def get(self, request):
        try:
            request_json = json.loads(request.body)
        except JSONDecodeError:
            return generate_json_response(False, {}, "Request body could not be parsed", status.HTTP_400_BAD_REQUEST)
        try:
            account_number = request_json["account_number"]
        except KeyError:
            return generate_json_response(False, {}, "account_number is missing.", status.HTTP_400_BAD_REQUEST)

        try:
            account = Account.objects.get(account_number=account_number)
            serializer = AccountSerializer(account, many=False)
            return generate_json_response(True, {"account": account.current_amount}, "Account Balance fetched Successfully",
                                          status.HTTP_200_OK)
        except Account.DoesNotExist:
            return generate_json_response(False, {}, "No such account found.", status.HTTP_404_NOT_FOUND)
