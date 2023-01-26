from django.urls import path
from regi import views
  
urlpatterns = [
    path("", views.sign),
    path("register", views.registration),
    path("glavnaya", views.glavnaya),
    path("strim", views.strim),
    path("gif", views.gif),
    path("video", views.video),
    path("strim1", views.strim1),
    path("strim2", views.strim2),
    path("strim3", views.strim3),
    path("strim4", views.strim4),
    path("strim5", views.strim5),
    path("strim6", views.strim6),
    path("video1", views.video1), 
    path("video2", views.video2), 
    path("video3", views.video3), 
    path("video4", views.video4), 
    path("video5", views.video5), 
    path("video6", views.video6),     
]