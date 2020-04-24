from django.shortcuts import render
from . models import Trivia
# Create your views here.

Class TriviaList(generics.ListAPIView):
    model = Trivia
    queryset = Trivia.objects.order_by('id')
