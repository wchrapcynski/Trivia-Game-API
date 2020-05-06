from rest_framework import serializers
from . models import TriviaQuestion, LeaderBoardRank

class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaQuestion
        fields = "__all__"

class LeaderBoardRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoardRank
        fields = "__all__"
