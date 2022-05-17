from django.shortcuts import render
from django.http import HttpResponse

products = [
    {
        'name': 'Coxinha de Frango',
        'cost': 'R$13,00'
    },
    {
        'name': 'Coxinha de Frango',
        'cost': 'R$13,00'
    },
    {
        'name': 'Coxinha de Frango',
        'cost': 'R$13,00'
    },
    {
        'name': 'Coxinha de Frango',
        'cost': 'R$13,00'
    }
]

def home(request):

    context = {
        'products': products
    }

    return render(request, 'shop/home.html', context)
