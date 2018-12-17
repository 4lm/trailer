from django.contrib import admin
from .models import Film, Trailer, Genre


class TrailerAdmin(admin.ModelAdmin):
    list_display = ['title', 'film']


class TrailerInline(admin.StackedInline):
    model = Trailer


class FilmAdmin(admin.ModelAdmin):
    inlines = [TrailerInline]


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'tmdb_id']


admin.site.register(Film, FilmAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Genre, GenreAdmin)
