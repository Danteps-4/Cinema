from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path("<str:pk>/", views.view, name="view")
]