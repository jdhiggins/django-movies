from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Rater, Rating, Movie

class RaterAdmin(admin.ModelAdmin):
    list_display = ['gender', 'age', 'zip_code']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rater', 'rating']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'genre']


admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Movie, MovieAdmin)