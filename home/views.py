from django.shortcuts import render
from django.http import HttpResponse #for simple responses

from . models import ResourceLink

# Create your views here.

def homepage(request):
    #return HttpResponse("literal html can go here")
    resource_links = ResourceLink.objects.all().order_by('title')
    return render(request, 'home/homepage.html', {'resource_links':resource_links})

def resource_info(request, title):
    this_resource = ResourceLink.objects.get(slug=title)
    return render(request, 'home/resource_detail.html', {'this_resource' : this_resource})
    #return HttpResponse('resource info' + str(title))

# def register(request, title):
#     reister = ResourceLink.objects.get(slug=title)
#     return render(request, 'home/register.html', {'this_user' : this_user})
#     #return HttpResponse('resource info' + str(title))
