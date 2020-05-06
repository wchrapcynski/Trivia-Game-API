from rest_framework import generics
from . serializers import TriviaSerializer, LeaderBoardRankSerializer
from . models import TriviaQuestion, LeaderBoardRank

class TriviaList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.order_by('id')
    serializer_class = TriviaSerializer

class LeaderBoardRankList(generics.ListAPIView):
    model = LeaderBoardRank
    queryset = LeaderBoardRank.objects.order_by('id')
    serializer_class = LeaderBoardRankSerializer
