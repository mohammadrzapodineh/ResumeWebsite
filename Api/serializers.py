from rest_framework import serializers
from Protfillo.models import Portfillo, Category


class ProtfilloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfillo
        fields = '__all__'


class CategorySeralizer(serializers.ModelSerializer):
    class Meta:
        moedel = Category 
        fields = '__all__'