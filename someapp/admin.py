from django.contrib import admin
from .models import Manufacturer, Product


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name", "country")
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "manufacturer")
    list_filter = ("manufacturer",)
    search_fields = ("name", "manufacturer__name")
    ordering = ("name",)
    list_select_related = ("manufacturer",)