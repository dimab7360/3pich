from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *
# Create your views here.
def index(requests):
    persh_str = Threepich.objects.all()[0:4]
    drug_str =  Threepich.objects.all()[5:8]
    osel =  Threepich.objects.all()[8:11]
    vmoch =  Threepich.objects.all()[11:14]
    napoi =  Threepich.objects.all()[14:21]
    return render(requests, 'Threepich/index.html', {'persh_str': persh_str , 'drug_str': drug_str , 'osel':osel, 'vmoch':vmoch, 'napoi':napoi})

# def menu(requests):
#     posts = Threepich.objects.all()
#     return render(requests, 'Threepich/menu.html', {'posts': posts})

def osel(requests):
    osel =  Threepich.objects.all()[21:31]
    return render(requests, 'Threepich/osel.html',{'osel':osel})


def about(requests):
    
    return render(requests, 'Threepich/about.html')