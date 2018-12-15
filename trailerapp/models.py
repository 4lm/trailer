from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    __repr__ = __str__


class Trailer(models.Model):
    title = models.CharField(max_length=255)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    __repr__ = __str__
