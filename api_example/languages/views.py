from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Language, Survey
from .serializers import LanguageSerializers, QuestionSerializer, SurveySerializer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializers
    


class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    
    @action(detail=True, methods=['get'], serializer_class=QuestionSerializer)
    def questions(self, request, pk=None):
        survey = self.get_object()
        serializer = self.get_serializer(survey.questions, many=True)

        return Response(serializer.data)