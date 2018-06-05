from django.db import models
from django_countries.fields import CountryField

question_types = (('free', 'Free Text'), ('options', 'Options'), ('check', 'Checkboxes'),
                  ('int', 'Integer'), ('decimal', 'Decimal'), ('boolean', 'Boolean'))

# Create your models here.


class Toolkit(models.Model):
    '''
    📚 · Database model for commodity toolkits (the base of questionnaires' sets)
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Pillar(models.Model):
    '''
    📗 · Database model for a questionnaire's pillar, which contains sections (sets) of questions
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=10, default="#D9D9C3")

    def __str__(self):
        return self.name


class Section(models.Model):
    '''
    📑 · Database model for a question set, related to a pillar
    '''
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pillar = models.ForeignKey(Pillar, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Question(models.Model):
    '''
    📜 · Database model for a single question, related to a section
    '''
    section = models.ForeignKey(Section, blank=True, null=True, on_delete=models.CASCADE)
    text = models.TextField()
    type = models.TextField(choices=question_types)

    def __str__(self):
        return '(%s) %s' % (self.section, self.text)


class Property(models.Model):
    '''
    🌄 · Database model for properties or houses
    '''
    class Meta:
        verbose_name_plural = 'properties'
    
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = CountryField(blank_label='(Select)')

    def __str__(self):
        return self.name


class Respondent(models.Model):
    '''
    🌰 · Database model for the individual who responds the questionnaire
    '''
    name = models.CharField(max_length=75)
    surname = models.CharField(max_length=175)
    birthdate = models.DateField()
    role = models.CharField(max_length=100)
    property = models.ManyToManyField(Property, blank=True)
    phone = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)
