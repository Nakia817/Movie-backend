from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import generics
# Create your views here.

class MovieList(generics.ListAPIView):
    queryset= Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetail(generics.RetrieveAPIView):
    queryset= Movie.objects.all()
    serializer_class = MovieSerializer
    

