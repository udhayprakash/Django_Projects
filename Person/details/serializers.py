from rest_framework import serializers
from details.models import Person, Gender

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    gender = GenderSerializer()

    class Meta:
        model = Person
        fields = '__all__'
