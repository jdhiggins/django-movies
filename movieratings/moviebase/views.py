from django.shortcuts import render
import operator
# Create your views here.
from .models import Movie, Rater, Rating
# Create your views here.


def top_movies(request):
    # movie_queryset = Movie.objects.all()
    # movie_ratings_dict = {m.title: m.average_rating() for m in movie_queryset}
    # sorted_movies = sorted(movie_ratings_dict.items(), key=operator.itemgetter(1), reverse=True)
    # if len(movie_queryset) < 10:
    #     movies = sorted_movies[:len(movie_queryset)]
    # else:
    #     movies = sorted_movies[:10]
#    movies_list = Movie.top_movies()
    return render(request, "moviebase/top_movies.html", name="top_movies")

#
# def show_user(request, user_id):
#     user = User.objects.get(user_id())
#     statuses = user.status_set
#     return render(request,
#                   "updates/user.html",
#                   {"user": user})

