from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Film, Trailer
from .services import get_data
import datetime
from trailerpress.settings import API_KEY, LANGUAGE, REGION


class FilmIndexListView(ListView):
    model = Film
    template_name = 'trailerapp/home.html'
    context_object_name = 'films'
    paginate_by = 5
    ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'TrailerPress'
        return context


@user_passes_test(lambda u: u.is_superuser)
def playing(request):
    films = {}
    if request.GET.get('get-btn'):
        api_key = API_KEY
        language = LANGUAGE
        page = 1
        region = REGION
        url = 'https://api.themoviedb.org/3/movie/now_playing'
        films['results'] = get_data(url, api_key, language, page, region)
        for film_result in films['results']:
            if len(film_result['videos_results']) is not 0:
                film = Film()
                film.title = film_result['title']
                film.original_title = film_result['original_title']
                film.language = language
                film.original_language = film_result['original_language']
                film.region = region
                film.overview = film_result['overview']
                film.release_date = film_result['release_date']
                film.tmdb_id = film_result['id']
                film.backdrop_path = film_result['backdrop_path']
                film.vote_average = 0
                film.vote_count = 0
                try:
                    film.save()
                except IntegrityError as e:
                    print(e)
                    pass
                for video_result in film_result['videos_results']:
                    if video_result['type'] is 'Trailer' or 'Teaser':
                        trailer = Trailer()
                        trailer.title = video_result['name']
                        trailer.film = Film.objects.get(tmdb_id=film_result['id'])
                        trailer.tmdb_id = video_result['id']
                        trailer.language = video_result['iso_639_1']
                        trailer.region = video_result['iso_3166_1']
                        trailer.site = video_result['site']
                        trailer.site_key = video_result['key']
                        trailer.type = video_result['type']
                        trailer.date_added = datetime.datetime.now()
                        try:
                            trailer.save()
                        except IntegrityError as e:
                            print(e)
                            pass
    return render(request, 'trailerapp/playing.html', {'films': films, 'page_title': 'Now Playing'})


@user_passes_test(lambda u: u.is_superuser)
def playing(request):
    films = {}
    if request.GET.get('get-btn'):
        api_key = API_KEY
        language = LANGUAGE
        page = 1
        region = REGION
        url = 'https://api.themoviedb.org/3/movie/now_playing'
        films['results'] = get_data(url, api_key, language, page, region)
        for film_result in films['results']:
            if len(film_result['videos_results']) is not 0:
                film = Film()
                film.title = film_result['title']
                film.original_title = film_result['original_title']
                film.language = language
                film.original_language = film_result['original_language']
                film.region = region
                film.overview = film_result['overview']
                film.release_date = film_result['release_date']
                film.tmdb_id = film_result['id']
                film.backdrop_path = film_result['backdrop_path']
                film.vote_average = 0
                film.vote_count = 0
                try:
                    film.save()
                except IntegrityError as e:
                    print(e)
                    pass
                for video_result in film_result['videos_results']:
                    if video_result['type'] is 'Trailer' or 'Teaser':
                        trailer = Trailer()
                        trailer.title = video_result['name']
                        trailer.film = Film.objects.get(tmdb_id=film_result['id'])
                        trailer.tmdb_id = video_result['id']
                        trailer.language = video_result['iso_639_1']
                        trailer.region = video_result['iso_3166_1']
                        trailer.site = video_result['site']
                        trailer.site_key = video_result['key']
                        trailer.type = video_result['type']
                        trailer.date_added = datetime.datetime.now()
                        try:
                            trailer.save()
                        except IntegrityError as e:
                            print(e)
                            pass
    return render(request, 'trailerapp/playing.html', {'films': films, 'page_title': 'Now Playing'})


@user_passes_test(lambda u: u.is_superuser)
def upcoming(request):
    films = {}
    if request.GET.get('get-btn'):
        api_key = API_KEY
        language = LANGUAGE
        page = 1
        region = REGION
        url = 'https://api.themoviedb.org/3/movie/upcoming'
        films['results'] = get_data(url, api_key, language, page, region)
        for film_result in films['results']:
            if len(film_result['videos_results']) is not 0:
                film = Film()
                film.title = film_result['title']
                film.original_title = film_result['original_title']
                film.language = language
                film.original_language = film_result['original_language']
                film.region = region
                film.overview = film_result['overview']
                film.release_date = film_result['release_date']
                film.tmdb_id = film_result['id']
                film.backdrop_path = film_result['backdrop_path']
                film.vote_average = 0
                film.vote_count = 0
                try:
                    film.save()
                except IntegrityError as e:
                    print(e)
                    pass
                for video_result in film_result['videos_results']:
                    if video_result['type'] is 'Trailer' or 'Teaser':
                        trailer = Trailer()
                        trailer.title = video_result['name']
                        trailer.film = Film.objects.get(tmdb_id=film_result['id'])
                        trailer.tmdb_id = video_result['id']
                        trailer.language = video_result['iso_639_1']
                        trailer.region = video_result['iso_3166_1']
                        trailer.site = video_result['site']
                        trailer.site_key = video_result['key']
                        trailer.type = video_result['type']
                        trailer.date_added = datetime.datetime.now()
                        try:
                            trailer.save()
                        except IntegrityError as e:
                            print(e)
                            pass
    return render(request, 'trailerapp/upcoming.html', {'films': films, 'page_title': 'Upcoming'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account for {} has been created! You are now able to log in'.format(username))
            return redirect('trailerapp:login')
    else:
        form = UserRegisterForm()
    return render(request, 'trailerapp/register.html', {'form': form})


def about(request):
    return render(request, 'trailerapp/about.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('trailerapp:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'trailerapp/profile.html', context)
