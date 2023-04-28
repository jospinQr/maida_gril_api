from rest_framework import serializers
from resto.models import product,product_categorie,unit_measure


class categSerialiser(serializers.ModelSerializer):
    class Meta:
        model=product_categorie
        fields="__all__"

class unitMSerializer(serializers.ModelSerializer):
    class Meta:
        model=unit_measure
        fields="__all__"  

class productSerialiser(serializers.ModelSerializer):

    class Meta:
        model=product
        fields="__all__"
