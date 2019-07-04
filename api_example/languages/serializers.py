from rest_framework import serializers
from .models import Question, SubQuestion, Answer, Language, Survey

class SubQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubQuestion
        fields = ('subQuestion', 'text')
    
    subQuestion = serializers.SerializerMethodField()

    def get_subQuestion(self, obj):
        return obj.order

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('order', 'text')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('survey', 'title', 'questions', 'answers')

    answers = AnswerSerializer(many=True)
    survey = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    def get_survey(self, obj):
        return obj.order

    def get_questions(self, obj):
        return SubQuestionSerializer(obj.sub_questions, many=True).data

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('questions',)

    questions = QuestionSerializer(many=True)

class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id','question_0_0',
                                   'question_0_1',
                                   'question_0_2',
                                   'question_0_3',
                                   'question_0_4',
                                   'question_0_5',
                                   'question_0_6',
                                   'question_0_7',
                                   'question_0_8',
                                   'question_0_9',
                                   'question_0_10',
                                   'question_0_11',
                                   'question_0_12',
                                   'question_0_13',
                                   'question_1_0',
                                   'question_1_1',
                                   'question_1_2',
                                   'question_1_3',
                                   'question_1_4',
                                   'question_1_5',
                                   'question_1_6',
                                   'question_1_7',
                                   'question_1_8',
                                   'question_2_0',
                                   'question_2_1',
                                   'question_2_2',
                                   'question_2_3',
                                   'question_2_4',
                                   'question_2_5',
                                   'question_2_6',
                                   'question_3_0',
                                   'question_3_1',
                                   'question_3_2',
                                   'question_3_3',
                                   'question_3_4',
                                   'question_3_5')