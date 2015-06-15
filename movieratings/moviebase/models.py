from django.db import models
import operator
from django.contrib.auth.models import User
from django.db.models import Avg, Count
# Create your models here.

class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              null=True)

    ONE = 1
    EIGHTEEN = 18
    TWENTY_FIVE = 25
    THIRTY_FIVE= 35
    FORTY_FIVE = 45
    FIFTY = 50
    FIFTY_SIX = 56
    AGE_CHOICES = (
        (ONE, "Under 18"),
        (EIGHTEEN, "18 to 25"),
        (TWENTY_FIVE, "25 to 34"),
        (THIRTY_FIVE, "35 to 44"),
        (FORTY_FIVE, "45 to 49"),
        (FIFTY, "50 to 55"),
        (FIFTY_SIX, "56+"),
    )
    age = models.IntegerField(choices=AGE_CHOICES)

    OTHER = 0
    ACADEMIC =  1
    ARTIST =  2
    CLERICAL =  3
    COLLEGE =  4
    CUSTOMER_SERVICE =  5
    HEALTH_CARE =  6
    EXECUTIVE =  7
    FARMER =  8
    HOMEMAKER =  9
    K_12 = 10
    LAWYER =  11
    PROGRAMMER = 12
    RETIRED = 13
    SALES_MARKETING = 14
    SCIENTIST = 15
    SELF_EMPLOYED = 16
    TECHNICIAN = 17
    TRADESMAN = 18
    UNEMPLOYED = 19
    WRITER = 20
    JOB_CHOICES = (
        (OTHER, "other"),
        (ACADEMIC, "academic/educator"),
        (ARTIST, "artist"),
        (CLERICAL, "clerical/admin"),
        (COLLEGE,  "college/grad student"),
        (CUSTOMER_SERVICE, "customer service"),
        (HEALTH_CARE, "doctor/health care"),
        (EXECUTIVE, "executive/managerial"),
        (FARMER, "farmer"),
        (HOMEMAKER, "homemaker"),
        (K_12, "K-12 student"),
        (LAWYER, "lawyer"),
        (PROGRAMMER,"programmer"),
        (RETIRED, "retired"),
        (SALES_MARKETING, "sales/marketing"),
        (SCIENTIST, "scientist"),
        (SELF_EMPLOYED, "self-employed"),
        (TECHNICIAN, "technician/engineer"),
        (TRADESMAN, "tradesman/craftsman"),
        (UNEMPLOYED, "unemployed"),
        (WRITER, "writer")
    )
    job=models.IntegerField(choices=JOB_CHOICES,
                            default=0,
                            null=True)

    zip_code = models.CharField(max_length=10,
                              null=True)

    user = models.OneToOneField(User, null=True)


    def num_reviews(self):
        #add if ratings
        return self.rating_set.count()

    def movies_seen(self):
        #add if ratings
        ratings = self.rating_set.all()
        return {rating.movie: rating.rating for rating in ratings}

    @property
    def average_rating(self):
        #add if ratings:
        ratings = self.rating_set.all()
        total = 0
        if ratings:
            for rating in ratings:
                total += rating.rating
            return round(total/len(ratings), 2)
        else:
            return "No ratings"

    @property
    def ratings_count(self):
        count_rating = self.rating_set.all().aggregate(Count('rating'))
        if count_rating:
            return (count_rating['rating__count'])
        else:
            return "No ratings"

    def __str__(self):
        return "UserID: {} || {} || {} || zip: {} || job: {}".format(self.id , self.gender, self.age, self.zip_code,
                                                                     self.job)


class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)
    genre = models.ManyToManyField(Genre)


    def __str__(self):
        return self.title
    # return "{}, || avg. rating: {}".format(self.title, self.average_rating())

    @property
    def average_rating(self):
    # ratings = self.rating_set.all()
        average_rating = self.rating_set.all().aggregate(Avg('rating'))
        if average_rating:
            return round(average_rating['rating__avg'], 2)
        else:
            return "No ratings"

    @property
    def ratings_count(self):
        count_rating = self.rating_set.all().aggregate(Count('rating'))
        if count_rating:
            return (count_rating['rating__count'])
        else:
            return "No ratings"



class Rating(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES=(
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5)
    )

    rating = models.IntegerField(choices=RATING_CHOICES,
                                 null=True)

    movie = models.ForeignKey(Movie, null=True)

    rater = models.ForeignKey(Rater, null=True)

    def __str__(self):
        return "{} reviewed {} || {} * rating.".format(self.rater.id, self.movie.title, self.rating)

    class Meta:
        unique_together = ('rater', 'movie')



class Genre(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"G
    CHILDREN = "Children's"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    FILM_NOIR = "Film-Noir"
    HORROR = "Horror"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCIFI = "Sci-Fi"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"
    GENRE_CHOICES = (
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (ANIMATION, "Animation"),
        (CHILDREN, "Children's"),
        (COMEDY, "Comedy"),
        (CRIME, "Crime"),
        (DOCUMENTARY, "Documentary"),
        (DRAMA, "Drama"),
        (FANTASY, "Fantasy"),
        (FILM_NOIR, "Film-Noir"),
        (HORROR, "Horror"),
        (MUSICAL, "Musical"),
        (MYSTERY, "Mystery"),
        (ROMANCE, "Romance"),
        (SCIFI, "Sci-Fi"),
        (THRILLER, "Thriller"),
        (WAR, "War"),
        (WESTERN, "Western")
    )

    genre = models.CharField(choices=GENRE_CHOICES,
                             null=True,
                             max_length=30)


def create_users():
    for rater in Rater.objects.all():
        user = User.objects.create_user('User{}'.format(rater.id),
                                        'user{}'.format(rater.id),
                                        '{}password'.format(rater.id))
        rater.user = user
        rater.save()


def change_emails():
    for user in User.objects.all():
        password = "password"
        user.set_password(password)
        user.save()


