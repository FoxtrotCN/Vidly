from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)


