from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('trivia/', views.TriviaList.as_view(), name='trivia_list'),
    path('categorysearch/', views.TriviaCategorySearch.as_view(), name='trivia_list'),
    path('question/<int:pk>', views.TriviaQuestion.as_view(), name='trivia_question'),
    path('published/', views.TriviaPublishedIdsList.as_view(), name='published'),
    path('leaderboard/', views.LeaderBoardRankList.as_view(), name='leader_board'),
    path('leaderboardupdate/', views.LeaderBoardRankUpdate.as_view(), name='leader_board_update')
]
