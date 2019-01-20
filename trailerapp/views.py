from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Film
from .services import save_data
from trailerpress.settings import API_KEY, LANGUAGE, REGION
from star_ratings.models import UserRating


class FilmIndexListView(ListView):
    model = Film
    template_name = 'trailerapp/home.html'
    context_object_name = 'films'
    paginate_by = 5
    ordering = ['-release_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'TrailerPress'
        return context


@user_passes_test(lambda u: u.is_superuser)
def get_films(request):
    api_key = API_KEY
    language = LANGUAGE
    page = 1
    region = REGION
    films = {}
    if request.GET.get('playing'):
        url = 'https://api.themoviedb.org/3/movie/now_playing'
        films = save_data(url, api_key, language, page, region)
    if request.GET.get('upcoming'):
        url = 'https://api.themoviedb.org/3/movie/upcoming'
        films = save_data(url, api_key, language, page, region)
    return render(request, 'trailerapp/get_films.html', {'films': films, 'page_title': 'Get Films'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Benutzerkonto für {} wurde erstellt! Sie können sich nun einloggen'.format(username))
            return redirect('trailerapp:login')
    else:
        form = UserRegisterForm()
    return render(request, 'trailerapp/register.html', {'form': form})


def about(request):
    return render(request, 'trailerapp/about.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Ihr Benutzerkonto wurde aktualisiert!')
            return redirect('trailerapp:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'ratings': UserRating.objects.filter(user=request.user)
    }

    return render(request, 'trailerapp/profile.html', context)
