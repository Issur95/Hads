"""
Definition of models.
"""

from django.db import models
from django.db.models.fields import CharField

# Create your models here.

TOPIC = [
    ('HADS Proyectos','HADS Proyectos'),
    ('Metodologia de la Asignatura', 'Metodologia de la Asignatura'),
    ('Django', 'Django'),
    ('Python', 'Python'),
    ('Alumnado','Alumnado'),
    ('Otras Asignaturas','Otras Asignaturas'),
]

class Topic(models.Model):
    topic = models.CharField(max_length=30, choices= [('Todos','Todos')] + TOPIC)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    topic = models.CharField(max_length=30, choices=TOPIC, default='Hads Proyectos')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correctChoice = models.BooleanField(default=False)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

   
