from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

from django.template import RequestContext, loader
from django.shortcuts import render


def index(request):
    context = {}
    try:
        name = request.POST['namestring']
        context["name"] = name
        return render(request, "mtest/index_post.html", context)
    except (KeyError):
        return render(request, 'mtest/index.html', context)









def namestring(request, name_string):
    response = "Hello," + name_string
    return HttpResponse(response)

    
