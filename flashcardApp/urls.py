from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from .views import getFlashcardsView
from django.contrib.auth import views as auth_views

app_name = "flashcardApp"

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('signIn/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signUp/', views.user_registration, name='registration'),
    path('flashcards/<str:groupId>/', views.flashcard, name='flashcards'),
    path('flashcardGroup/<str:title_pk>/', views.flashcard_group_view, name='flashcardGroup'),
    path('getFlashcards/<str:groupId>', getFlashcardsView.as_view(), name='getFlashcards'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)