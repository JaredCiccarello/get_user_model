from django.urls import path

from .views import HomePageView, AboutPageView, GamePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("game-list/", GamePageView.as_view(), name="game-list"),
]
