from django.shortcuts import render
from django.http import HttpResponse
from .models import Fmovies

def index(request):
    obj = Fmovies.objects.all()
    context = {
        "obj":obj, 
    }
    return render(request, "index.html", context)


