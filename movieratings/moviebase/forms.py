__author__ = 'joshuahiggins'
from django import forms
from django.contrib.auth.models import User
from .models import Rater, Rating

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #hides password when typed

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RaterForm(forms.ModelForm):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    gender = forms.ChoiceField(choices = GENDER_CHOICES, label="Gender", initial='',
                               widget=forms.Select(), required=True)

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
    age = forms.ChoiceField(choices = AGE_CHOICES, label="Age", initial='',
                               widget=forms.Select(), required=True)

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
    job = forms.ChoiceField(choices = JOB_CHOICES, label="Job", initial='',
                               widget=forms.Select(), required=True)

    class Meta:
        model = Rater
        fields = ('gender', 'age', 'job', 'zip_code')


class RatingForm(forms.ModelForm):
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

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               initial='',
                               widget=forms.Select(),
                               required=True)


    class Meta:
        model = Rating
        fields = ('rating',)


class EditForm(forms.ModelForm):
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

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               initial='',
                               widget=forms.Select(),
                               required=True)


    class Meta:
        model = Rating
        fields = ('rating',)


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('rating', 'model', 'rater')
