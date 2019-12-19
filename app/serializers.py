from rest_framework import serializers
from . import models

class TodoSerializer(serializers.ModelSerializer):
  """"Create Serializer for TODO LISTS"""
  class Meta:
    model = models.TodoList
    fields = ('id', 'title', 'body',)
