from django.contrib import admin
from . models import TriviaQuestion
from . models import LeaderBoardRank

class TriviaAdmin(admin.ModelAdmin):
    fields = ['question', 'answers']
    list_display = ['question', 'answers']

admin.site.register(TriviaQuestion)

class LeaderBoardRankAdmin(admin.ModelAdmin):
    fields = ['email', 'score', 'date']
    list_display = ['email', 'score', 'date']

admin.site.register(LeaderBoardRank)
