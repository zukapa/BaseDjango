from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {'title': 'GeekShop-Каталог', 'category': ProductCategory.objects.all()}
    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    context.update({'products': product})
    return render(request, 'products/products.html', context)
