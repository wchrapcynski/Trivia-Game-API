from rest_framework import generics
from random import randint
from . serializers import TriviaQuestionSerializer, LeaderBoardRankSerializer, TriviaQuestionPublishedIdsSerializer
from . models import TriviaQuestion, LeaderBoardRank

class TriviaList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionSerializer

class TriviaPublishedIdsList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionPublishedIdsSerializer

class LeaderBoardRankList(generics.ListAPIView):
    model = LeaderBoardRank
    queryset = LeaderBoardRank.objects.order_by('id')
    serializer_class = LeaderBoardRankSerializer
