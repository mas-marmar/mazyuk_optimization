from django.shortcuts import render, aget_list_or_404
from .models import Product, Manufacturer
from asyncio import create_task


async def my_view(request):
    products_task = create_task(aget_list_or_404(Product))
    manufacturers_task = create_task(aget_list_or_404(Manufacturer))

    products = await products_task
    manufacturers = await manufacturers_task

    return render(request, "./index.html", {
        "products": products,
        "manufacturers": manufacturers,
    })