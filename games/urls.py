from django.urls import path
from games.views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

urlpatterns = [
    path('', GameListView.as_view(), name='list_view'),
    path('<int:pk>', GameDetailView.as_view(), name='detail_view'),
    path('new', GameCreateView.as_view(), name='create_view'),
    path('<int:pk>/edit', GameUpdateView.as_view(), name='update_view'),
    path('<int:pk>/delete', GameDeleteView.as_view(), name='delete_view'),
]