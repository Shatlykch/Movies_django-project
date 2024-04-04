
from .serializers import MovieSerializer, ReviewsSerializer
# Define the home view
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Reviews


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to the movies-collector api home route!'}
        return Response(content)


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewsListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewsSerializer

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Reviews.objects.filter(movie_id=movie_id)

    def perform_create(self, serializer):
        movie_id = self.kwargs['movie_id']
        movie = Movie.objects.get(id=movie_id)
        serializer.save(movie=movie)


class ReviewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Reviews.objects.filter(movie_id=movie_id)
