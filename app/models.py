from django.db import models

class TodoList(models.Model):

  title = models.CharField(max_length=250)
  body = models.TextField()

  def __str__(self):
    return self.title

  

