# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search_results/<str:search_term>/", views.search_view, name="search_results"),
    path("search_redirect/", views.search_redirect, name="search_redirect"),
    path("payments", views.initiateKhalti, name="payments")
]
