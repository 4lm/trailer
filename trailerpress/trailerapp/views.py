from django.shortcuts import render
from .models import Film

def index(request):
    films = Film.objects.all().order_by('title')

    return render(request, 'trailerapp/index.html', {'page_title': 'TrailerPress', 'films': films})
