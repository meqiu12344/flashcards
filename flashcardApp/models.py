from datetime import datetime

from django.contrib import auth
from django.contrib.auth.models import User, Permission, Group
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', null=True, blank=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, help_text='')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, help_text='')


class FlashcardGroup(models.Model):
    title = models.CharField(max_length=250)
    cardQuantity = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    groupManager = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flashcardApp:flashcardGroup', args=[self.title])


class Flashcard(models.Model):
    word = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    group = models.ForeignKey(FlashcardGroup, on_delete=models.CASCADE)
    language = models.CharField(max_length=250, default='')

    flashcardManager = models.Manager()