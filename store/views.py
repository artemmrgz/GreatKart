from django.shortcuts import render, get_object_or_404
from category.models import Category
from .models import Product

def store(request, category_slug=None):
    if category_slug != None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
        count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        count = products.count()

    context = {'products': products, 'product_count': count}
    return render(request, 'store.html', context=context)
