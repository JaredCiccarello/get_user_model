from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Game
from django.urls import reverse_lazy
  

# Create your views here.

class GameListView(ListView):
    template_name = 'game-list.html'
    model = Game
    context_object_name = 'games'


class GameDetailView(DetailView):
    template_name = 'game-detail.html'
    model = Game


class GameCreateView(CreateView):
    template_name = 'game-create.html'
    model = Game
    fields = ['name', 'description', 'owner']


class GameUpdateView(UpdateView):
    template_name = 'game-update.html'
    model = Game
    fields = ['name', 'description', 'owner']


class GameDeleteView(DeleteView):
    template_name = 'game-delete.html'
    model = Game
    success_url = reverse_lazy('game-list')