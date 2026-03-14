from django.urls import path

from cinema.views import MovieViewSet, ActorViewSet, GenreViewSet, CinemaHallViewSet

methods_list = {
    'get': 'list',
    'post': 'create'
}

methods_details = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}

movie_list = MovieViewSet.as_view(methods_list)
movie_detail = MovieViewSet.as_view(methods_details)
actor_list = ActorViewSet.as_view(methods_list)
actor_detail = ActorViewSet.as_view(methods_details)
genre_list = GenreViewSet.as_view(methods_list)
genre_detail = GenreViewSet.as_view(methods_details)
cinema_hall_list = CinemaHallViewSet.as_view(methods_list)
cinema_hall_detail = CinemaHallViewSet.as_view(methods_details)

urlpatterns = [
    path("movies/", movie_list, name="movie-list"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path("actors/", actor_list, name="actor-list"),
    path("actors/<int:pk>/", actor_detail, name="actor-detail"),
    path("genres/", genre_list, name="genre-list"),
    path("genres/<int:pk>/", genre_detail, name="genre-detail"),
    path("cinema-halls/", cinema_hall_list, name="cinema-hall-list"),
    path("cinema-halls/<int:pk>/", cinema_hall_detail, name="cinema-hall-detail"),
]

app_name = "cinema"
