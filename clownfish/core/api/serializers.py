from rest_framework.serializers import ModelSerializer
from core.models import Toolkit, Pillar, Section, Question, Property, Respondent


class ToolkitSerializer(ModelSerializer):
    class Meta:
        model = Toolkit
        # fields = ('id', 'name', 'description')
        fields = '__all__'


class PillarSerializer(ModelSerializer):
    class Meta:
        model = Pillar
        fields = '__all__'


class SectionSerializer(ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class RespondentSerializer(ModelSerializer):
    class Meta:
        model = Respondent
        fields = '__all__'
