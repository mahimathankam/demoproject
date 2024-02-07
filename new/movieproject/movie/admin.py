from django.contrib import admin
from movie.models import Movie
from django.http import HttpResponse
admin.site.register(Movie)
