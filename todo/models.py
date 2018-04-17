from django.db import models
from datetime import datetime


class Todo(models.Model):
    text = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    mydate = models.DateTimeField(auto_now=False, auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
