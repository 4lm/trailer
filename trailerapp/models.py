from django.db import models


class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Film(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=8, null=True)  # iso_639_1
    original_language = models.CharField(max_length=8, null=True)  # iso_639_1
    region = models.CharField(max_length=8, null=True)  # iso_3166_1
    overview = models.TextField(null=True)
    release_date = models.DateTimeField(null=True)
    tmdb_id = models.CharField(max_length=64, null=True, unique=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)
    backdrop_path = models.CharField(max_length=255, null=True)
    poster_path = models.CharField(max_length=255, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    __repr__ = __str__


class Trailer(models.Model):
    title = models.CharField(max_length=255)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    tmdb_id = models.CharField(max_length=64, null=True, unique=True)
    language = models.CharField(max_length=8, null=True)  # iso_639_1
    region = models.CharField(max_length=8, null=True)  # iso_3166_1
    site = models.CharField(max_length=64, null=True)  # origin of video
    site_key = models.CharField(max_length=64, null=True)  # key of video at origin
    type = models.CharField(max_length=10, null=True)  # Trailer|Teaser
    date_added = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    __repr__ = __str__
