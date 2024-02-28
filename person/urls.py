from django.urls import path
from . import views

app_name = "person"

urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
]