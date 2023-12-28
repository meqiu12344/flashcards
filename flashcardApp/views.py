from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from flashcardApp.forms import LoginForm, RegistrationForm
from flashcardApp.models import flashcardGroup, flashcard


# Create your views here.
def Index(request):
    return render(request, 'content/index.html')


def User_login(request):
    loginError = False
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                loginError = True
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form, 'loginError': loginError})


def User_registration(request):
    error = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                User.objects.create_user(
                    username=request.POST.get('username'),
                    email=request.POST.get('email'),
                    password=request.POST.get('password'),
                    first_name=request.POST.get('name'),
                )

            except:
                error = True
        else:
            error = True
    else:
        form = RegistrationForm()

    return render(request, 'user/registration.html', {'form': form, 'error': error})


def Create(request):
    if request.method == 'POST':
        lesson_name = request.POST['lesson-name']
        polish_words = request.POST.getlist('polish[]')
        english_words = request.POST.getlist('english[]')

        username = request.user.username

        new_flashcard_group = flashcardGroup.groupManager.create(
            title=lesson_name,
            cardQuantity=len(polish_words),
            author=User.objects.get(username=username)
        )

        for polish, english in zip(polish_words, english_words):
            flashcard.flashcardManager.create(
                word=polish,
                answer=english,
                group=new_flashcard_group,
                language='Angielski',
            )

        return HttpResponseRedirect('/search/')
    else:
        return render(request, 'content/create.html', {})


def Search(request):
    allFlashCardGroups = flashcardGroup.groupManager.all()
    return render(request, 'content/search.html', {'allGroups': allFlashCardGroups})


def FlashcardGroupView(request, title_pk):
    group = get_object_or_404(flashcardGroup, title=title_pk)
    flashcards = flashcard.flashcardManager.filter(group=group)
    return render(request, 'content/flashcard-group.html', {'group': group, 'flashcards': flashcards})


def Flashcard(request, groupId):
    group = get_object_or_404(flashcardGroup, title=groupId)
    flashcards = flashcard.flashcardManager.filter(group=group)
    return render(request, 'content/flashcard.html', {'flashcards': flashcards, 'group': group})


class getFlashcardsView(View):
    def get(self, request, groupId):
        group = get_object_or_404(flashcardGroup, title=groupId)
        flashcardsJson = flashcard.flashcardManager.filter(group=group).values()

        return JsonResponse({'flashcardsJson': list(flashcardsJson)})