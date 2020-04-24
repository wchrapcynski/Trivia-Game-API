from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.TriviaList.as_view(), name='trivia_list')
]
