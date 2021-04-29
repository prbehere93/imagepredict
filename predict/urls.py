from django.urls import path
from . import views #imports views from the current directory

urlpatterns = [
    path("", views.home, name='home'),
    ]
