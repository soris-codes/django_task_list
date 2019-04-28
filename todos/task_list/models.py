from django.db import models
from django.utils import timezone

class Task(models.Model):
  text = models.CharField(max_length=200)
  complete = models.BooleanField(default=False)

  def __str__(self):
    return self.text
