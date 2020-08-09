from rest_framework import generics, mixins
import django_filters.rest_framework
from random import randint
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from . serializers import TriviaQuestionSerializer, LeaderBoardRankSerializer
from . models import TriviaQuestion, LeaderBoardRank


class TriviaList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionSerializer


class TriviaPublishedIdsList(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionSerializer

    def list(self, request):
        return Response(self.get_queryset().values_list("id",))


class TriviaCategorySearch(generics.ListAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['category']


class TriviaQuestion(generics.RetrieveAPIView):
    model = TriviaQuestion
    queryset = TriviaQuestion.objects.filter(published=True).order_by('id')
    serializer_class = TriviaQuestionSerializer


class LeaderBoardRankList(generics.ListAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin):

    lookup_field = 'id'

    model = LeaderBoardRank
    queryset = LeaderBoardRank.objects.order_by('-score')[:3]
    serializer_class = LeaderBoardRankSerializer

    def post(self, request):
        return self.create(request)

    def put(self, request, id):
        return self.update(request, id)
