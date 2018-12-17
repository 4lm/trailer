from django.contrib.auth.decorators import user_passes_test
from django.db import IntegrityError
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Film, Trailer
from .services import get_data
import datetime
from trailerpress.settings import API_KEY


class FilmIndexListView(ListView):
    model = Film
    template_name = 'trailerapp/home.html'
    context_object_name = 'films'
    paginate_by = 5
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'TrailerPress'
        return context


@user_passes_test(lambda u: u.is_superuser)
def playing(request):
    films = {}
    if request.GET.get('get-btn'):
        api_key = API_KEY
        language = 'de'
        page = 1
        region = 'DE'
        films['results'] = get_data(api_key, language, page, region)
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
