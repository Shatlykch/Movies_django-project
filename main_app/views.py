
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MovieSerializer
# Define the home view
from rest_framework import generics
from .models import Movie


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
