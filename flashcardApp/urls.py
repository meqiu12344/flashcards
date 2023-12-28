from django.urls import path
from . import views
from .views import getFlashcardsView
from django.contrib.auth import views as auth_views

app_name = "flashcardApp"

urlpatterns = [
    path('', views.Index, name='index'),
    path('create/', views.Create, name='create'),
    path('search/', views.Search, name='search'),
    path('signIn/', views.User_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signUp/', views.User_registration, name='registration'),
    path('flashcards/<str:groupId>/', views.Flashcard, name='flashcards'),
    path('flashcardGroup/<str:title_pk>/', views.FlashcardGroupView, name='flashcardGroup'),
    path('getFlashcards/<str:groupId>', getFlashcardsView.as_view(), name='getFlashcards'),
]