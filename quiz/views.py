from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Quizz
from .serializers import QuizzSerializer

# Create your views here.
class QuizzList(generics.ListCreateAPIView):

    queryset = Quizz.objects.all()
    serializer_class = QuizzSerializer

