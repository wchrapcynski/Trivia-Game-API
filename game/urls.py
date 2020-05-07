from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('trivia', views.TriviaList.as_view(), name='trivia_list'),
    path('leaderboard', views.LeaderBoardRankList.as_view(), name='leader_board'),
    path('published', views.TriviaPublishedIdsList.as_view(), name='published')
]
