from django.urls import path
from . import views

app_name = 'trailerapp'
urlpatterns = [
    path('', views.FilmIndexListView.as_view(), name='film-list'),
    path('register/', views.register, name='register'),
    path('playing/', views.playing, name='playing'),
]
