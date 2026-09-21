from django.db import models


class Manufacturer(models.Model):
    name = models.CharField("Название", max_length=255)
    country = models.CharField("Страна", max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Название", max_length=255)
    price = models.DecimalField("Цена", max_digits=100000, decimal_places=2)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Производитель")
    
    def __str__(self):
        return self.name
