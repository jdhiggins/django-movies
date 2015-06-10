from django.shortcuts import render
import operator
# Create your views here.
from .models import Movie, Rater, Rating
# Create your views here.


def top_movies(request):
    movie_queryset = Movie.objects.all()
    movie_ratings_dict = {m: m.average_rating for m in movie_queryset if isinstance(m.average_rating, float)}
    sorted_movies = sorted(movie_ratings_dict.items(), key=operator.itemgetter(1), reverse=True)
    movies = [movie[0] for movie in sorted_movies]
    movies = movies[:20]
    return render(request, "moviebase/top_movies.html",
                  {"movies": movies})


def show_rater(request, rater_id):
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    return render(request,
                  "moviebase/rater.html",
                  {"rater": rater,
                   "ratings": ratings})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = movie.rating_set.all()
    return render(request,
                  "moviebase/movie.html",
                  {"movie": movie,
                   "ratings": ratings})