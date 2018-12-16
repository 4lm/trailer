from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, null=True)
    language = models.CharField(max_length=8, null=True)  # iso_639_1
    region = models.CharField(max_length=8, null=True)  # iso_3166_1
    overview = models.TextField(null=True)
    release_date = models.DateTimeField(null=True)
    tmdb_id = models.CharField(max_length=64, null=True)
    vote_average = models.FloatField(null=True)
    vote_count = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    __repr__ = __str__


class Poster(models.Model):
    file_path = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    vote_average = models.FloatField()  # origin tmbd


class Genre(models.Model):
    tmdb_id = models.IntegerField()
    name = models.CharField(max_length=64)
    films = models.ManyToManyField(Film)

    def __str__(self):
        return self.name

    __repr__ = __str__


class Trailer(models.Model):
    title = models.CharField(max_length=255)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    tmdb_id = models.CharField(max_length=64, null=True)
    language = models.CharField(max_length=8, null=True)  # iso_639_1
    region = models.CharField(max_length=8, null=True)  # iso_3166_1
    site = models.CharField(max_length=64, null=True)  # origin of video
    site_key = models.CharField(max_length=64, null=True)  # key of video at origin
    type = models.CharField(max_length=10, null=True)  # Trailer|Teaser
    date_added = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    __repr__ = __str__
