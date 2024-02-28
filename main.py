import json
import requests
import shutil
from movie.movie import Movie

url = "https://api.themoviedb.org/3/authentication"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlNTMzM2U5NDgxMzFhZjM5ZDAxYmJjYmNkZTUzOWY3ZiIsInN1YiI6IjY1ZDZjMmUxNjA5NzUwMDE4NTI0YjM0OCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Lbsf_hlgMEQK-Ja5BVnwLnAVL9khDamOk0aOnQKvB9g"
}

response = requests.get(url, headers=headers)

# print(response.text)

def search_movie(movie_name, page):
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_name}&page={page}"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["results"]
    # print(json_result)
    return json_result

def get_movie_details(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)
    # print(json_result)
    return json_result

def get_movie_image(path):
    url = "https://image.tmdb.org/t/p/w500/{path}"

    response = requests.get(url, stream=True)
    print(response.raw)

def get_trending_movies(time_window):
    url = f"https://api.themoviedb.org/3/trending/movie/{time_window}"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["results"]
    return json_result

def get_popular_movies():
    url = "https://api.themoviedb.org/3/movie/popular"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["results"]
    return json_result

def get_movie_cast(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["cast"]
    return json_result

def get_recommendations_on_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["results"]
    return json_result

def get_reviews_on_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["results"]
    return json_result

def get_review(review_id):
    url = f"https://api.themoviedb.org/3/review/{review_id}"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_person(person_id):
    url = f"https://api.themoviedb.org/3/person/{person_id}"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def get_url_of_image(image_path):
    url = f"https://image.tmdb.org/t/p/w500/{image_path}"
    return url

def get_available_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["genres"]
    return json_result

def get_available_languages():
    url = "https://api.themoviedb.org/3/configuration/languages"

    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

def minutes_to_hours(minutes):
    hours = minutes//60
    minu = minutes%60
    string = f"{str(hours)}h {str(minu)}m"
    return string

if __name__ == "__main__":
    # for movie in get_trending_movies("week"):
    #     print(movie)

    # movies = search_movie("avatar", 1)
    # for movie in movies:
    #     print(movie["title"])

    # movie = get_trending_movies("day")[0]
    # movie = get_movie_details(movie["id"])
    # for genre in movie["genres"]:
    #     print(genre["name"])

    # get_movie_image("AbFtI353N2Pggl5TxfsI2VtpUt8.jpg")
    
    # movie_detail = get_movie_details(969492)
    # movie = Movie(969492, movie_detail["title"], movie_detail["tagline"], movie_detail["genres"], movie_detail["overview"], movie_detail["release_date"], movie_detail["vote_average"])
    # print(movie.genres)
    # print(movie_detail["genres"])
    # cast = get_movie_cast(969492)
    # for person in cast:
    #     print(person["name"])
    # recommendations = get_recommendations_on_movie(969492)
    # for recommendation in recommendations:
    #     print(recommendation["title"])

    cast = get_movie_cast(969492)
    print(cast[0]["id"])