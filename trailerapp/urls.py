from django.urls import path
from . import views

app_name = 'trailerapp'
urlpatterns = [
    path('playing/', views.playing, name='playing'),
    path('', views.FilmIndexListView.as_view(), name='film-list'),
]
