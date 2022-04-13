from django.urls import  path
from . import views

urlpatterns= [
    path("", views.landing, name="landing"),
    path("rates/<int:pk>/", views.solution, name="solution"),
    path("contact/<int:pk>/", views.contact, name="contact"),
    path("about", views.about_us, name="about"),
    ]