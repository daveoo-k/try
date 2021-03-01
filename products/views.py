from django.shortcuts import render
from django.http import HttpResponse
from .form import ProductForm
from .models import Product

def product_detail_view (request, *args,**kwargs):
    obj = Product.objects.get(id=3 )
    context = {
        'title' : obj.title,
        'description': obj.description,
        'price': obj.price,
        'features' : obj.features,
        'summary' : obj.summary
    }
    return render(request,"product/detail.html",context)

def product_create_view (request,*args,**kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form':form
    }  
    return render(request,"product/create.html",context) 
# Create your views here.