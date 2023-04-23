from rest_framework import serializers
from languages.models import Language

class LanguageSerializer(serializers.HyperlinkedModelSerializer): # ModelSerializer
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')