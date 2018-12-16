from django.contrib import admin
from .models import Film, Trailer, Genre, Poster


class TrailerAdmin(admin.ModelAdmin):
    list_display = ['title', 'film']


class TrailerInline(admin.StackedInline):
    model = Trailer


class FilmAdmin(admin.ModelAdmin):
    inlines = [TrailerInline]


admin.site.register(Film, FilmAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Genre)
admin.site.register(Poster)
