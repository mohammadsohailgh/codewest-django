from django.contrib.auth.models import User
from django.db import models

# change Language to surveyresult

class Survey(models.Model):
    description = models.TextField(blank=False, null=False)
    name = models.CharField(blank=False, null=False, max_length=100)

class Question(models.Model):
    order = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, related_name='questions', blank=False, null=False)
    title = models.TextField(blank=False, null=False)

class SubQuestion(models.Model):
    order = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='sub_questions', blank=False, null=False)
    text = models.TextField(blank=False, null=False)

class Answer(models.Model):
    order = models.PositiveSmallIntegerField(blank=False, null=False, default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', blank=False, null=False)
    text = models.TextField(blank=False, null=False)

class SurveyData(models.Model):
    # app_user = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=False, null=False)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

class SavedAnswer(models.Model):
    survey_data = models.ForeignKey(SurveyData, on_delete=models.CASCADE, related_name='saved_answers', blank=False, null=False)
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.CASCADE, blank=False, null=False)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=False, null=False)

class Language(models.Model): 
    question_0_0 = models.CharField(max_length=25, default='Not answered')
    question_0_1 = models.CharField(max_length=25, default='Not answered')
    question_0_2 = models.CharField(max_length=25, default='Not answered')
    question_0_3 = models.CharField(max_length=25, default='Not answered')
    question_0_4 = models.CharField(max_length=25, default='Not answered')
    question_0_5 = models.CharField(max_length=25, default='Not answered')
    question_0_6 = models.CharField(max_length=25, default='Not answered')
    question_0_7 = models.CharField(max_length=25, default='Not answered')
    question_0_8 = models.CharField(max_length=25, default='Not answered')
    question_0_9 = models.CharField(max_length=25, default='Not answered')
    question_0_10 = models.CharField(max_length=25, default='Not answered')
    question_0_11 = models.CharField(max_length=25, default='Not answered')
    question_0_12 = models.CharField(max_length=25, default='Not answered')
    question_0_13 = models.CharField(max_length=25, default='Not answered')

    question_1_0 = models.CharField(max_length=25, default='Not answered')
    question_1_1 = models.CharField(max_length=25, default='Not answered')
    question_1_2 = models.CharField(max_length=25, default='Not answered')
    question_1_3 = models.CharField(max_length=25, default='Not answered')
    question_1_4 = models.CharField(max_length=25, default='Not answered')
    question_1_5 = models.CharField(max_length=25, default='Not answered')
    question_1_6 = models.CharField(max_length=25, default='Not answered')
    question_1_7 = models.CharField(max_length=25, default='Not answered')
    question_1_8 = models.CharField(max_length=25, default='Not answered')

    question_2_0 = models.CharField(max_length=25, default='Not answered')
    question_2_1 = models.CharField(max_length=25, default='Not answered')
    question_2_2 = models.CharField(max_length=25, default='Not answered')
    question_2_3 = models.CharField(max_length=25, default='Not answered')
    question_2_4 = models.CharField(max_length=25, default='Not answered')
    question_2_5 = models.CharField(max_length=25, default='Not answered')
    question_2_6 = models.CharField(max_length=25, default='Not answered')

    question_3_0 = models.CharField(max_length=25, default='Not answered')
    question_3_1 = models.CharField(max_length=25, default='Not answered')
    question_3_2 = models.CharField(max_length=25, default='Not answered')
    question_3_3 = models.CharField(max_length=25, default='Not answered')
    question_3_4 = models.CharField(max_length=25, default='Not answered')
    question_3_5 = models.CharField(max_length=25, default='Not answered')










    def __str__(self):
        return self.name