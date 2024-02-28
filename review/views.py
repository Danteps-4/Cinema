from django.shortcuts import render
import main

# Create your views here.
def view(request, pk):
    review = main.get_review(pk)
    return render(request, "review/view.html", {"review": review})