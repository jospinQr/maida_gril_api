from django.shortcuts import render
from rest_framework import viewsets
from .models import product,product_categorie,unit_measure
from .serializer import categSerialiser, productSerialiser,unitMSerializer



class categViewSet(viewsets.ModelViewSet):

  queryset=product_categorie.objects.all()
  serializer_class=categSerialiser


class unitViewSet(viewsets.ModelViewSet):
  queryset=unit_measure.objects.all()
  serializer_class=unitMSerializer
  lookup_field="IdProdCat"

class productViewSet(viewsets.ModelViewSet):
  queryset=product.objects.all()
  serializer_class=productSerialiser
  


