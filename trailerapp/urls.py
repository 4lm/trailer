from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'trailerapp'
urlpatterns = [
    path('', views.FilmIndexListView.as_view(), name='film-list'),
    path('login/', auth_views.LoginView.as_view(template_name='trailerapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='trailerapp/logout.html'), name='logout'),
    path('playing/', views.playing, name='playing'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
