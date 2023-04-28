from django.db import models


class product_categorie(models.Model):
    IdProdCat= models.CharField(max_length=200, unique=True)
    Designation= models.CharField(max_length=200, unique=True)
    Description= models.TextField(max_length=500)
    def __str__(self):
        return self.Designation

class unit_measure(models.Model):
    IdUnitMes= models.CharField(max_length=200, unique=True)
    Designation= models.CharField(max_length=200)
    lotQuantity= models.FloatField()
    description = models.CharField(max_length= 500)

    def __str__(self):
        return self.Designation
    


class product(models.Model):
    idProd = models.CharField(max_length=200, unique=True)
    IdProdCat = models.ForeignKey(
        product_categorie, null=True, on_delete=models.CASCADE)
    IdUniteMes = models.ForeignKey(
        unit_measure, null=True, on_delete=models.DO_NOTHING)
    Designation = models.CharField(max_length= 200)
    Image = models.ImageField(null=True, blank=True)
    Price = models.FloatField()
    QtAlert = models.FloatField()
    Desciption=models.TextField(max_length=500)
    
    def __str__(self):
        return self.Designation
