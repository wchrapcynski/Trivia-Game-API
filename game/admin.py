from django.contrib import admin
from . import models

class TriviaQuestionAdmin(admin.ModelAdmin):
    fields = ['category', 'question', 'answer', 'choice1', 'choice2', 'choice3', 'choice4', 'published']
    list_display = ['question', 'category', 'published', 'id']
    search_fields = ['question', 'category']
    list_editable = ['published']

admin.site.register(models.TriviaQuestion, TriviaQuestionAdmin)


class LeaderBoardRankAdmin(admin.ModelAdmin):
    fields = ['email', 'score', 'date']
    list_display = ['email', 'score', 'date']

admin.site.register(models.LeaderBoardRank, LeaderBoardRankAdmin)
