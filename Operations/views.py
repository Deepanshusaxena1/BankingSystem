# Create your views here.
import json
from rest_framework import status
from rest_framework.views import APIView
from Operations.models import Customer
from Operations.serializers import CustomerSerializer
from Operations.utils import generate_json_response


class CustomerAPI(APIView):

    def get(self, request):
        request_json = json.loads(request.body)
        try:
            customer_id = request_json["customer_id"]
        except KeyError:
            return generate_json_response(False, {}, "customer_id is missing.", status.HTTP_400_BAD_REQUEST)
        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer, many=False)
            return generate_json_response(True, {"customer": serializer.data}, "Customer fetched Successfully",
                                          status.HTTP_200_OK)
        except Customer.DoesNotExist:
            return generate_json_response(False, {}, "No such customer found.", status.HTTP_404_NOT_FOUND)

        # return generate_json_response(False, {}, "Some error occurred", status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            generate_json_response(True, {"customer": serializer.data}, "Customer created Successfully.",
                                   status.HTTP_201_CREATED)
        else:
            generate_json_response(False, {}, serializer.errors, status.HTTP_400_BAD_REQUEST)

        return generate_json_response(False, {}, "Some error occurred", status.HTTP_500_INTERNAL_SERVER_ERROR)
