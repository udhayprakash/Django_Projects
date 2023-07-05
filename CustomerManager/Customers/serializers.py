from Customers.models import CustomerDetails
from rest_framework import serializers


class CustomerDetailsSerializer(serializers.HyperlinkedModelSerializer):  # ModelSerializer
    class Meta:
        model = CustomerDetails
        fields = ('id', 'url',
                  'name', 'first_name', 'telephone_number', 'date_of_contact')
