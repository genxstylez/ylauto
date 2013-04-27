from django.shortcuts import render, get_object_or_404
from product.models import Category, Model
from collections import OrderedDict

def categories(request):
    categories = Category.objects.all()
    return render(request, 'product/categories.html', {'categories': categories})


def model(request, model_id):
    model = get_object_or_404(Model, id=model_id)
    a = model.products.order_by('year')
    products = {}
    for product in a:
        if product.year not in products:
            year_products = a.filter(year=product.year)
            products[product.year] = year_products

    products = OrderedDict(sorted(products.items(), key=lambda t: t[0]))
    return render(request, 'product/model.html', {'model': model, 'products': products})
