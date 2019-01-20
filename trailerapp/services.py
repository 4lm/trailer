import requests
import datetime
from .models import Film, Trailer
from django.db import IntegrityError


def get_data(url: str, api_key: str, language: str, page: int, region: str):
    params = {'api_key': api_key, 'language': language, 'page': page, 'region': region}
    r = requests.get(url, params=params)
    data = r.json()
    counter = data['total_pages']
    if counter > 5:
        counter = 5
    results = []
    while counter > 0:
        params = {'api_key': api_key, 'language': language, 'page': counter, 'region': region}
        r = requests.get(url, params=params)
        data = r.json()
        for item in data['results']:
            results.append(item)
        counter -= 1
    if len(results) is not 0:
        for result in results:
            url = 'https://api.themoviedb.org/3/movie/' + str(result['id']) + '/videos'
            params = {'api_key': api_key, 'language': language}
            r = requests.get(url, params=params)
            data = r.json()
            result['videos_results'] = data['results']
    return results


def save_data(url: str, api_key: str, language: str, page: int, region: str):
    films = {}
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
    return films
