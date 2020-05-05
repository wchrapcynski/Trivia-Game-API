from django.db import models
from django.utils import timezone
from django_mysql.models import ListTextField

class TriviaQuestion(models.Model):
    question = models.TextField(null=True)
    answers = ListTextField(
        base_field=models.CharField(max_length=300),
        size=4,
        max_length=(6 * 11)
    )
    category = models.CharField(max_length=300, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.question

class LeaderBoardRank(models.Model):
    email = models.EmailField(max_length=254)
    score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.email
