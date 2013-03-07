from django.shortcuts import render, get_object_or_404
from product.models import Category, Model

def categories(request):
    categories = Category.objects.all()
    return render(request, 'product/categories.html', {'categories': categories})


def model(request, model_id):
    model = get_object_or_404(Model, id=model_id)
    return render(request, 'product/model.html', {'model': model})
