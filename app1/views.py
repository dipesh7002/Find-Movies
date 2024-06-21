from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Fmovies, HindiMovies, Onehd
from django.core import serializers
import requests
import json
movie_list = [Fmovies, HindiMovies, Onehd]
movie_urls = ["https://ww4.fmovies.co/movies/", "https://www.hindimovies.to/all-movies", "https://en.uwatchfree-official.lol/movies?page=1"]

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
def urls_verify(request):
    for movie_url in movie_urls:
        pass

def search_redirect(request):
    search_term = request.GET.get('q')
    
    if search_term:
        return redirect('search_results', search_term = search_term)
    else:
        return HttpResponse("Please enter a search term", status=400)

def index(request):
    return render(request, "search_page.html", {})

def initiateKhalti(request):
    
    url = "https://a.khalti.com/api/v2/epayment/initiate/"
    return_url = request.POST.get('return_url')
    purchase_order_id = request.POST.get('purchase_order_id')
    amount = request.POST.get('amount')

    print("return url", return_url)
    print("purchase_order_id", purchase_order_id)
    print("amount", amount)
    

    payload = json.dumps({
        "return_url": return_url,
        "website_url": "http://http://127.0.0.1:8000",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "test",
        "customer_info": {
        "name": "Dipesh Regmi",
        "email": "dipeshregmi999@gmail.com",
        "phone": "9800000001"
        }
    })
    headers = {
        'Authorization': 'key test_secret_key_3b0dc759b1af4f6cbb53138eb2410a63',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    new_res = json.loads(response.text)
    print("This is khalti", new_res)
    return redirect("search_redirect")
