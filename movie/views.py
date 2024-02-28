from django.shortcuts import render
import main
from .movie import Movie

# Create your views here.
def detail(request, pk):
    movie_detail = main.get_movie_details(pk)
    image_path = main.get_url_of_image(movie_detail["poster_path"])
    movie = Movie(movie_detail["id"], movie_detail["title"], movie_detail["tagline"], movie_detail["genres"], movie_detail["overview"], movie_detail["release_date"], movie_detail["vote_average"], main.minutes_to_hours(int(movie_detail["runtime"])), main.get_movie_cast(movie_detail["id"]), main.get_recommendations_on_movie(movie_detail["id"]), main.get_reviews_on_movie(movie_detail["id"]), image_path)
    return render(request, "movie/detail.html", {"movie": movie})

def movies(request):
    popular_movies = main.get_popular_movies()
    genres = main.get_available_genres()
    languages = main.get_available_languages()
    return render(request, "movie/movies.html", {"movies": popular_movies, "genres": genres, "languages": languages})

def all_reviews(request, pk):
    reviews = main.get_reviews_on_movie(pk)
    movie = main.get_movie_details(pk)
    return render(request, "movie/all_reviews.html", {"reviews":reviews, "movie": movie})