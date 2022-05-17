from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'shop/home.html', context)
