from django.test import TestCase
from .models import Film, Trailer
from uuid import uuid4


class FilmModelTests(TestCase):

    def test_str(self):
        '''
            Test __str__ method of model Film.
        '''
        uuid = uuid4()
        test_film = Film(title=uuid)
        self.assertEqual(test_film.__str__(), uuid)


class TrailerModelTests(TestCase):

    def test_str(self):
        '''
            Test __str__ method of model Trailer.
        '''
        uuid = uuid4()
        test_trailer = Trailer(title=uuid)
        self.assertEqual(test_trailer.__str__(), uuid)
