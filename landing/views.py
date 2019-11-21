from django.shortcuts import render
from django.http import HttpResponse
from .forms import SubscriberForm
from django.template import RequestContext

def index(request):
    return HttpResponse('kykyk')

def landing(request):
    form = SubscriberForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        data = form.cleaned_data
        print(data['name'])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals(), RequestContext(request))