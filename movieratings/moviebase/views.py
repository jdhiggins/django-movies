from django.shortcuts import render
import operator
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating
# Create your views here.


def top_movies(request):
    # movie_queryset = Movie.objects.all()
    # movie_ratings_dict = {m: m.average_rating for m in movie_queryset if isinstance(m.average_rating, float)}
    # sorted_movies = sorted(movie_ratings_dict.items(), key=operator.itemgetter(1), reverse=True)
    # movies = [movie[0] for movie in sorted_movies]
    # movies = movies[:20]
    # First Try Above.  It worked, but was really slow.
    #
    # movies = Movies.objects.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    # Second Try Above.  It also worked, but I wanted to add functionality to it to filter by number of ratings
    #
    movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating')[:20]
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


# The top 5 publishers, in order by number of books.
#movies = Movie.objects.annotate(average_rating=Avg('rating')).order_by('-average_rating')[:20]
