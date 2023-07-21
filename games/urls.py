from django.urls import path
from games.views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('game', GameListView.as_view(), name='game-list'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('new', GameCreateView.as_view(), name='game-create'),
    path('<int:pk>/edit', GameUpdateView.as_view(), name='game-update'),
    path('<int:pk>/delete', GameDeleteView.as_view(), name='game-delete'),
]