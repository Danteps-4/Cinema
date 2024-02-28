from django.shortcuts import render, redirect
import main

# Create your views here.
def home(request):
    trending_movies_day = main.get_trending_movies("day")[:5]
    popular_movies = main.get_popular_movies()[:5]
    return render(request, "core/home.html", {"trending_movies_day": trending_movies_day, "popular_movies": popular_movies})

def search(request):
    query = request.GET.get("query", "")
    print(query)
    if query:
        movies = main.search_movie(query, 1)
        return render(request, "core/search.html", {"query": query, "movies": movies})
    else:
        return redirect("core:home")
    