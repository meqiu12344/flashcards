from datetime import datetime

from django.contrib import auth
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse


class flashcardGroup(models.Model):
    title = models.CharField(max_length=250)
    cardQuantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    groupManager = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flashcardApp:flashcardGroup', args=[self.title])


class flashcard(models.Model):
    word = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    group = models.ForeignKey(flashcardGroup, on_delete=models.CASCADE)
    language = models.CharField(max_length=250, default='')

    flashcardManager = models.Manager()