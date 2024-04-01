from rest_framework import serializers
from .models import EnumarationGeography, IndividualDetails


class EnumarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnumarationGeography
        fields='__all__'


class IndividualDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualDetails
        fields='__all__'