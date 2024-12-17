from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("grid_display/", views.grid_display, name="grid_display"),
    path("submission/", views.submission, name="submission"),
    path("results/", views.results, name="results"),
]