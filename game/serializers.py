from rest_framework import serializers
from . models import TriviaQuestion

class TriviaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TriviaQuestion
        fields = "__all__"
