from django.shortcuts import render
from rest_framework import generics

from . import models
from . import serializers


# class TodoListView(generics.ListAPIView):
#   queryset = models.TodoList.objects.all()
#   serializer_class = serializers.TodoSerializer

# class TodoDetailView(generics.RetrieveAPIView):
#   queryset = models.TodoList.objects.all()
#   serializer_class = serializers.TodoSerializer


class TodoListView(generics.ListCreateAPIView):
  queryset = models.TodoList.objects.all()
  serializer_class = serializers.TodoSerializer

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.TodoList.objects.all()
  serializer_class = serializers.TodoSerializer
