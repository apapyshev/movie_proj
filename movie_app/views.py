from django.shortcuts import render, get_object_or_404
from .models import Movie
from django.db.models import F, Sum, Avg, Min, Max, Count
# Create your views here.

def show_all_movie(requests):
    movies = Movie.objects.order_by(F('year').asc(nulls_last=True), 'rating')
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
    return render(requests, 'movie_app/all_movie.html',
    {
        'movies' : movies,
        'agg': agg
    })

def show_one_movie(requests, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(requests, 'movie_app/one_movie.html',
    {
        'movie': movie,
    })