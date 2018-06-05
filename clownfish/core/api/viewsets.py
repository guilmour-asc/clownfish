from rest_framework.viewsets import ModelViewSet
from core.models import Toolkit, Pillar, Section, Question, Property, Respondent
from .serializers import ToolkitSerializer, PillarSerializer, SectionSerializer, QuestionSerializer, PropertySerializer, RespondentSerializer


class ToolkitViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Toolkits.
    """
    queryset = Toolkit.objects.all()
    serializer_class = ToolkitSerializer


class PillarViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Pillars.
    """
    queryset = Pillar.objects.all()
    serializer_class = PillarSerializer


class SectionViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Sections.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class QuestionViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PropertyViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Questions.
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class RespondentViewSet(ModelViewSet):
    """
    Clownfish's viewset for querying Questions.
    """
    queryset = Respondent.objects.all()
    serializer_class = RespondentSerializer
