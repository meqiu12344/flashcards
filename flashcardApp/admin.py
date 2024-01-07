from django.contrib import admin
from flashcardApp.models import FlashcardGroup, Flashcard
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class customUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'profile_picture']


@admin.register(FlashcardGroup)
class flashcardGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'cardQuantity', 'date', 'author']


@admin.register(Flashcard)
class flashcardGroupAdmin(admin.ModelAdmin):
    list_display = ['word', 'answer', 'group', 'language']