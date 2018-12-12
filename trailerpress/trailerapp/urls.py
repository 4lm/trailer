from django.urls import path
from . import views

app_name = 'trailerapp'
urlpatterns = [
    path('', views.index, name='index'),
]
