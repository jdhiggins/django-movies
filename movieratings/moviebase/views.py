import operator
from django.db.models import Avg, Count
from .models import Movie, Rater, Rating, Genre
from .forms import UserForm, RaterForm, RatingForm, EditForm, DeleteForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AnonymousUser
from django.core.paginator import Paginator
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
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating').select_related()[:20]
    # rated_movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
    #     ('rating__rating')).order_by('-num_ratings').select_related()[:20]
    # genres = Genre.objects.all()
    return render(request, "moviebase/top_movies.html",
                  {"movies": movies})
    # Have to do rating__rating because rating has relationship to movie as ForeignKey, otherwise can just do rating
    #    as in    count_rating = self.rating_set.all().aggregate(Count('rating'))
    #   -avg_rating means reverse the order
    #   should look up num_ratings__gt  i think thats just how you filter by num_ratings
    #   filter will pull only the things you ask for, exclude will pull the other stuff
    #   annotate derives data from database and returns it  __ if you are looking in a related model
    # gt is greater than, gte is greater than or equal to


def most_movies(request):
    rated_movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).order_by('-num_ratings').select_related()[:20]
    return render(request, "moviebase/most_movies.html",
                  {"rated_movies": rated_movies})


def all_genres(request):
    genres = Genre.objects.all()
    return render(request, "moviebase/all_genres.html",
                  {"genres": genres})


def show_rater(request, rater_id):
    movies = Movie.objects.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating')
    rater = Rater.objects.get(pk=rater_id)
    ratings = rater.rating_set.all()
    movie_set = [rating.movie for rating in ratings]
    movies_not_seen = [movie for movie in movies if movie not in movie_set]
    return render(request,
                  "moviebase/rater.html",
                  {"rater": rater,
                   "ratings": ratings,
                   "movies_not_seen": movies_not_seen[:20]})


def show_movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    ratings = Rating.objects.filter(movie=movie).select_related('rater').all()
    #if null is true for Rater, have to put Rater in select_related
    # ratings_set = [rating.movie for rating in request.user.rater.rating_set.all()]
    #
    # rating_dict = {rating.movie: rating for rating in request.user.rater.rating_set.all()}
    # if movie in ratings_set:
    #     user_rating = rating_dict[movie]
    # else:
    #     user_rating = None
    #_____________________________

    ratings_paginator = Paginator(ratings, 30)

    user = request.user

    try:
        user_rating = Rating.objects.get(rater_id=user.rater.id, movie_id=movie_id)
    except:
        user_rating = None

    page=request.GET.get('page',1)
    rating_form = RatingForm()
    edit_form = EditForm()
    return render(request,
                  "moviebase/movie.html",
                  {"movie": movie,
                   #"ratings": ratings,
                   "ratings": (ratings_paginator.page(page)),
                   #see movie.html
                   "rating_form": rating_form,
                   #
                   "user_rating": user_rating,
                   "edit_form": edit_form
                   })


def show_genre(request, genre_id):
    genre = Genre.objects.get(pk=genre_id)
    movies = genre.movie_set.select_related().all()
    top_genre = movies.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).filter(num_ratings__gt=30).order_by('-avg_rating').select_related()[:20]
    most_genre = movies.annotate(avg_rating=Avg('rating__rating')).annotate(num_ratings=Count
        ('rating__rating')).order_by('-num_ratings').select_related()[:20]
    return render(request, "moviebase/genre.html",
                  {"top_genre": top_genre,
                   "most_genre": most_genre,
                   "genre": genre})



def user_register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        rater_form = RaterForm(data=request.POST)

        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save()
            password = user.password
            user.set_password(password)
            user.save()

            rater = rater_form.save(commit=False)
            rater.user = user
            rater.save()

            registered = True

            user = authenticate(username=user.username,
                                password=password)
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Welcome, {}! You are now registered at MovieBase.".format(user.username)
            )
            return redirect('top_movies')

    else:
        user_form = UserForm()
        rater_form = RaterForm()

    return render(request,
                  "moviebase/register.html",
                  {'user_form': user_form,
                   'rater_form': rater_form})



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/moviebase/')


def make_rating(request, movie_id):

    if request.method == 'POST':
        rating_form = RatingForm(data=request.POST)

        if rating_form.is_valid():
            movie = Movie.objects.get(pk=movie_id)
            rating = rating_form.save(commit=False)
            rating.rater = request.user.rater
            rating.movie = movie
            rating.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "You have registered a review of {}".format(rating.movie)
            )
        return redirect('show_rater', request.user.rater.id)
    else:
        rating_form = RatingForm()

    return render(request,
                  "moviebase/movie/{}.html".format(movie_id),
                  {'rating_form': rating_form})

def edit_rating(request, movie_id, rating_id):
    user_rating = Rating.objects.get(pk=rating_id)
    if request.method == 'POST':

        edit_form = EditForm(data=request.POST, instance = user_rating)

        if edit_form.is_valid():
            rating = edit_form.save(commit=False)
            rating.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                "You have registered a review of {}".format(rating.movie)
            )
        return redirect('show_rater', request.user.rater.id)
    else:
        edit_form = EditForm(instance=user_rating)

    return render(request,
                  "moviebase/movie/{}.html".format(movie_id),
                  {'edit_form': edit_form})



def delete_rating(request, movie_id, rating_id):
    user_rating = Rating.objects.get(pk=rating_id)
    movie = user_rating.movie
    if request.method == 'POST':
        user_rating.delete()

        messages.add_message(
                request,
                messages.SUCCESS,
                "You have DELETED a review of {}".format(movie)
            )
        return redirect('show_rater', request.user.rater.id)
    else:
        delete_form = DeleteForm(instance=user_rating)

    return render(request,
                  "moviebase/movie/{}.html".format(movie_id),
                  {'delete_form': delete_form})


def get_rater(user):
    """Gets the profile for a user. Ensures profile exists."""
    if type(user) == AnonymousUser:
        return None
    else:
        try:
            rater = user.rater
        except Rater.DoesNotExist:
            rater = Rater()
            rater.user = user
            rater.save()
        finally:
            return rater
