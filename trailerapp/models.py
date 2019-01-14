from django.db import models
from django.contrib.auth.models import User
from PIL import Image


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '{} Profile'.format(self.user.username)

    __repr__ = __str__

    def save(self, force_insert=False, force_update=False, using=None):
        super().save()

        img = Image.open(self.image.path)
        max_width, max_height = 300, 300

        if img.height > max_height or img.width > max_width:
            if img.height >= img.width:
                aspect_ratio = img.height / img.width
                output_size = (max_width, max_height * aspect_ratio)
            else:
                aspect_ratio = img.width / img.height
                output_size = (max_width * aspect_ratio, max_height)
            img.thumbnail(output_size)
            if img.height is not img.width:
                width, height = img.size
                left = (width - max_width) / 2
                top = (height - max_height) / 2
                right = (width + max_width) / 2
                bottom = (height + max_height) / 2
                cropped_img = img.crop((left, top, right, bottom))
                cropped_img.save(self.image.path)
        else:
            img.save(self.image.path)
