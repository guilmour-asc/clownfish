from django.contrib import admin
from .models import Toolkit, Pillar, Section, Question, Property, Respondent

# Register your models here.
admin.site.register([Toolkit, Pillar, Section, Question, Property, Respondent])
