# coding: utf-8
from movie_app.models import Movie
movie = Movie.objects.create(
name = "Not Winner",
rating=87,
year=2016,
budget= 1820000,
currency="usd",
)
Movie.save()
