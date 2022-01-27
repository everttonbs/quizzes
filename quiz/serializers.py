from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Quizz

class QuizzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizz
        fields = ('question', )
