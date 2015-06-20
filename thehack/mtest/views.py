from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello.")


def namestring(request, name_string):
    response = "Hello," + name_string
    return HttpResponse(response)

    
