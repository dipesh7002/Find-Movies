from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fmovies
from .models import HindiMovies
from django.core import serializers

movie_list = [Fmovies, HindiMovies]

def search_view(request, search_term):
    search_results = []
    search_terms = search_term.lower().split(' ')
    for movie in movie_list:
        movie_all = movie.objects.all()
        for movies in movie_all:
            if any(term in movies.movie_name.lower() for term in search_terms):
                search_results.append({
                    "movie_name": movies.movie_name,
                    "movie_link": movies.movie_link
                })
    return render(request, "index.html", {
        "search_term": search_term,
        "search_results": search_results
    })


def search_redirect(request):
    search_term = request.GET.get('q')
    
    if search_term:
        return redirect('search_results', search_term = search_term)
    else:
        return HttpResponse("Please enter a search term", status=400)

def index(request):
    return render(request, "search_page.html", {})
