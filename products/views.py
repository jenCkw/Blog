from django.shortcuts import render
from .models import Product
import uuid



def products(request):
    pr = Product.objects.all()
    return render(request, 'products/products.html', {'products': pr})


def detail(request, id):
    product = Product.objects.get(uuid=id)
    return render(request, 'products/detail.html', {'product':product})
    

# Create your views here.
