from django.urls import  path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns= [
    path("", views.landing, name="landing"),
    path("rates/<int:pk>/", views.solution, name="solution"),
    path("contact/<int:pk>/", views.contact, name="contact"),
    path("about", views.about_us, name="about"),
    path("CaseStudy/<int:pk>/", views.CaseStudy, name="case"),
    path("Contact", views.Contact, name="contact"),
    path("services", views.Services, name="services"),
    path("SingleDetail/<int:pk>/", views.SingleService, name="single"),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)