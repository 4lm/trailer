from django.test import Client, TestCase
from .models import Film, Genre, Trailer
from .views import FilmIndexListView
from uuid import uuid4


class FilmModelTests(TestCase):
    '''
        Film model tests.
    '''

    def test_str(self):
        '''
            Test __str__ method of model Film.
        '''
        uuid = uuid4()
        test_film = Film(title=uuid)
        self.assertEqual(test_film.__str__(), uuid)


class TrailerModelTests(TestCase):
    '''
        Trailer model tests.
    '''

    def test_str(self):
        '''
            Test __str__ method of model Trailer.
        '''
        uuid = uuid4()
        test_trailer = Trailer(title=uuid)
        self.assertEqual(test_trailer.__str__(), uuid)


class GenreModelTests(TestCase):
    '''
        Genre model tests.
    '''

    def test_str(self):
        uuid = uuid4()
        test_genre = Genre(name=uuid)
        self.assertEqual(test_genre.__str__(), uuid)


class FilmIndexListViewTests(TestCase):
    '''
        FilmIndexListView tests.
    '''

    def setUp(self):
        self.client = Client()

    def test_context_of_film_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page_title'], 'TrailerPress')

    def test_film_index_model(self):
        film_index = FilmIndexListView()
        self.assertEqual(film_index.model, Film)

    def test_film_index_template_name(self):
        film_index = FilmIndexListView()
        self.assertEqual(film_index.template_name, 'trailerapp/home.html')

    def test_film_index_context_object_name(self):
        film_index = FilmIndexListView()
        self.assertEqual(film_index.context_object_name, 'films')

    def test_film_index_context_pagination(self):
        film_index = FilmIndexListView()
        self.assertEqual(film_index.paginate_by, 5)

    def test_film_index_ordering(self):
        film_index = FilmIndexListView()
        self.assertEqual(film_index.ordering[0], 'title')
