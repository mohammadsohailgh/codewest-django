from django.contrib import admin
from .models import Question, SubQuestion, Answer, Language, Survey, SurveyData, SavedAnswer

admin.site.register(Language)
admin.site.register(Question)
admin.site.register(SubQuestion)
admin.site.register(Answer)
admin.site.register(Survey)
admin.site.register(SurveyData)
admin.site.register(SavedAnswer)

# Register your models here.
