from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), #to go to homepage
    path("projects/", views.projects, name="projects"),
    path("prediction_here/", views.contact, name="prediction_here"), #contact coz fn defined on view
]
