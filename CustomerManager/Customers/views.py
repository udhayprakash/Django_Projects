from Customers.models import CustomerDetails
from Customers.serializers import CustomerDetailsSerializer
from rest_framework import viewsets


class CustomerDetailsView(viewsets.ModelViewSet):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer
