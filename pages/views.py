from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Product

def home_page(request: HttpRequest ) -> HttpResponse:
    products = Product.objects.all()
    return render(request=request, template_name='index.html', context={'products':products})