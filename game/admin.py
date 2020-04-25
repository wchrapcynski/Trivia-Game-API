from django.contrib import admin
from . models import TriviaQuestion

class TriviaAdmin(admin.ModelAdmin):
    fields = ['question', 'answers']
    list_display = ['question', 'answers']

admin.site.register(TriviaQuestion)
