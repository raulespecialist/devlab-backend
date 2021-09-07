from django.shortcuts import render
from .models import Product, Service
from itertools import chain

#Dashboard view
def dashboard(request):
    products = Product.objects.all()
    services = Service.objects.all()
    return render(request, 'pos/dashboard.html', {'services': services, 'products': products})
# Buy view
def buy(request):
    #company = Company.objects.get(id=num)
    return render(request, 'pos/base.html')

# Catalogue view
def catalogue(request):
    products = Product.objects.all()
    services = Service.objects.all()
    proser = list(chain(products, services))
    return render(request, 'pos/catalogue.html', {'proserv': proser, 'services': services, 'products': products})
    #return render(request, 'pos/catalogue.html', {'products': producters})
