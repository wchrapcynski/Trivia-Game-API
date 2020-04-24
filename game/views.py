from rest_framework import generics
from . serializers import TriviaSerializer
from . models import Trivia

class TriviaList(generics.ListAPIView):
    model = Trivia
    queryset = Trivia.objects.order_by('id')
