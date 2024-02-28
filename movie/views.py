from django.shortcuts import render
import main
from .movie import Movie

# Create your views here.
def detail(request, pk):
    movie_detail = main.get_movie_details(pk)
    movie = Movie(movie_detail["id"], movie_detail["title"], movie_detail["tagline"], movie_detail["genres"], movie_detail["overview"], movie_detail["release_date"], movie_detail["vote_average"], main.minutes_to_hours(int(movie_detail["runtime"])), main.get_movie_cast(movie_detail["id"]), main.get_recommendations_on_movie(movie_detail["id"]), main.get_reviews_on_movie(movie_detail["id"]))
    return render(request, "movie/detail.html", {"movie": movie})

def all_reviews(request, pk):
    reviews = main.get_reviews_on_movie(pk)
    movie = main.get_movie_details(pk)
    return render(request, "movie/all_reviews.html", {"reviews":reviews, "movie": movie})