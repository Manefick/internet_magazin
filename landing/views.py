from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm
from django.template import RequestContext
from products.models import *

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals(), RequestContext(request))

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phone = products_images.filter(product__category__name='Телефоны')
    products_images_laptops = products_images.filter(product__category_id=2)
    return render(request, 'landing/home.html', locals(), RequestContext(request))