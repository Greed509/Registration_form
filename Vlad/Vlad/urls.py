from django.urls import path
from regi import views
  
urlpatterns = [
    path("", views.index),
    path("registration", views.registration),
]