from django.shortcuts import render
from .models import product
from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def list_products(request):
    """
    Returns product list page as HTML
    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=product.objects.all()
    product_paginator = Paginator(product_list,10)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request, 'products.html',context)

def detail_product(request):
    return render(request, 'product_detail.html')
