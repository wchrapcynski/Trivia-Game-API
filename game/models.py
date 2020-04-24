from django.db import models
from django_mysql.models import ListTextField

class Trivia(models.Model):
    question = models.TextField()
    answers = models.ListTextField(
        base_field=TextField(),
        size=4
    )
    published = models.BooleanField(default=False)
