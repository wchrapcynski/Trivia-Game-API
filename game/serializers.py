from rest_framework import serializers
from . models import TriviaQuestion, LeaderBoardRank

class TriviaQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaQuestion
        fields = "__all__"

class TriviaQuestionPublishedIdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaQuestion
        fields = ["id"]

class LeaderBoardRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardRank
        fields = "__all__"
