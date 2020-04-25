from rest_framework import generics
from . serializers import TriviaSerializer
from . models import TriviaQuestion

class TriviaList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.order_by('id')
    serializer_class = TriviaSerializer
