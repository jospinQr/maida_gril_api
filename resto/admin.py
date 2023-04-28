from django.contrib import admin
from resto.models import product_categorie, product, unit_measure

admin.site.register(product_categorie)
admin.site.register(unit_measure)
admin.site.register(product)
