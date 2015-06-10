from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Rater, Rating, Movie

class RaterAdmin(admin.ModelAdmin):
    list_display = ['gender', 'age', 'num_reviews', 'average_rating', 'zip_code']

class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'rater', 'rating']
    fieldsets = [
        ('Rating information',  {'fields': ['rater', 'rating']}),
        ('Movie information',    {'fields': ['movie']}),
    ]
    list_filter = ['rater']

class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'average_rating']
    search_fields = ['title']


admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Movie, MovieAdmin)