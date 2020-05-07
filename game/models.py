from django.db import models
from django.utils import timezone

class TriviaQuestion(models.Model):
    category = models.CharField(max_length=50, null=True)
    published = models.BooleanField(default=False)
    question = models.TextField(max_length=160, null=True)
    answer = models.IntegerField(choices=((0, 'Choice1'), (1, 'Choice2'), (2, 'Choice3'), (3, 'Choice4')), default=0)
    choice1 = models.TextField(max_length=55, null=True)
    choice2 = models.TextField(max_length=55, null=True)
    choice3 = models.TextField(max_length=55, null=True)
    choice4 = models.TextField(max_length=55, null=True)

    def __str__(self):
        return self.question

class LeaderBoardRank(models.Model):
    email = models.EmailField(max_length=254)
    score = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.email
