# import Home view from the views file
# additional imports
from .views import Home, MovieList, MovieDetail, ReviewsDetail, ReviewsListCreate
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
    path('movies/<int:movie_id>/reviews/<int:id>/',
         ReviewsListCreate.as_view(), name='reviews-list-create'),
    path('movies/<int:movie_id>/reviews/<int:id>/',
         ReviewsDetail.as_view(), name='reviews-detail'),

]
