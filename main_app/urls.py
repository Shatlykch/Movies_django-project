# import Home view from the views file
from .views import Home, MovieList, MovieDetail  # additional imports
from .views import Home
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
]

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # new routes below
    path('movies/', MovieList.as_view(), name='cat-list'),
    path('movies/<int:id>/', MovieDetail.as_view(), name='movie-detail'),
]
