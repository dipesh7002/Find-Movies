from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fmovies
from django.core import serializers

def search_view(request, search_term):
    Fmovies_all = Fmovies.objects.all()

    AllFmovies = serializers.serialize('json', Fmovies_all)
    results = []
    for fmovies in Fmovies_all:
        if search_term == fmovies.movie_name:
            results.append(fmovies.movie_link)
    if not results:
        results = ["No results whatsoever"]

    return render(request, "index.html",    {
        "search_term": search_term,
        "results": results

    })

def search_redirect(request):
    search_term = request.GET.get('q')
    if search_term:
        return redirect('search_results', search_term = search_term)
    else:
        return HttpResponse("Please enter a search term", status=400)

def index(request):
    return render(request, "search_page.html", {})
