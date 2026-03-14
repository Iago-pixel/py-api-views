from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, ActorViewSet, GenreViewSet, CinemaHallViewSet

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"actors", ActorViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"cinema-halls", CinemaHallViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"
