from django.urls import path
from regi import views
from django.views.generic import TemplateView
  
urlpatterns = [
    path("", views.sign),
    path("register", views.registration),
    path("glavnaya", TemplateView.as_view(template_name="glavnaya.html")), 
    path("strim", TemplateView.as_view(template_name="strim.html")), 
    path("gif", TemplateView.as_view(template_name="gif.html")), 
    path("video", TemplateView.as_view(template_name="video.html")), 
    path("strim1", TemplateView.as_view(template_name="strim1.html")), 
    path("strim2", TemplateView.as_view(template_name="strim2.html")), 
    path("strim3", TemplateView.as_view(template_name="strim3.html")), 
    path("strim4", TemplateView.as_view(template_name="strim4.html")), 
    path("strim5", TemplateView.as_view(template_name="strim5.html")), 
    path("strim6", TemplateView.as_view(template_name="strim6.html")), 
    path("video1", TemplateView.as_view(template_name="video1.html")), 
    path("video2", TemplateView.as_view(template_name="video2.html")), 
    path("video3", TemplateView.as_view(template_name="video3.html")), 
    path("video4", TemplateView.as_view(template_name="video4.html")), 
    path("video5", TemplateView.as_view(template_name="video5.html")), 
    path("video6", TemplateView.as_view(template_name="video6.html")),
]