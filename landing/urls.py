from django.urls import  path
from . import views

urlpatterns= [
    path("", views.landing, name="landing"),
    path("rates/<int:pk>/", views.solution, name="solution")
    ]