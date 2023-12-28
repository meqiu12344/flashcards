from django.contrib import admin
from flashcardApp.models import flashcardGroup, flashcard


# Register your models here.
@admin.register(flashcardGroup)
class flashcardGroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'cardQuantity', 'date', 'author']


@admin.register(flashcard)
class flashcardGroupAdmin(admin.ModelAdmin):
    list_display = ['word', 'answer', 'group', 'language']