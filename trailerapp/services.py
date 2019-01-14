import requests


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
