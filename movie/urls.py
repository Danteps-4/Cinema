from django.urls import path, include
from . import views

app_name = "movie"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/reviews/", views.all_reviews, name="all_reviews"),
]