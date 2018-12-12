from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Film


class FilmIndexListView(ListView):
    model = Film
    template_name = 'trailerapp/home.html'
    context_object_name = 'films'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'TrailerPress'
        return context
