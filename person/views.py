from django.shortcuts import render
import main

# Create your views here.
def detail(request, pk):
    person = main.get_person(pk)
    profile_path = main.get_url_of_image(person["profile_path"])
    return render(request, "person/detail.html", {"person": person, "profile_path": profile_path})