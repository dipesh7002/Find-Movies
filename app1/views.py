from django.shortcuts import render
from .models import Fmovies
from django.core import serializers
def index(request):
    Fmovies_all = Fmovies.objects.all()
    print(request.method)
    AllFmovies = serializers.serialize('json', Fmovies_all)
    context = {
        "AllFmovies":AllFmovies,

    }
    return render(request, "index.html", context)

# function that takes a request and gives back a response

from django.http import HttpRequest, HttpResponse
def index(request: HttpRequest):
    return HttpResponse("welcome")

def detail(request: HttpRequest) -> HttpResponse:
    return HttpResponse("polls details page: ")
