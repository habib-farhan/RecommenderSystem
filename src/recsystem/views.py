from django.contrib.auth import authenticate, login
from django.core import serializers
from django.contrib.auth import logout
from django.http import HttpResponse
from django.http import JsonResponse
import logging
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import  UserForm, QuestionForm, AnswerForm, FollowUpForm
from .models import Question, Answer, FollowUp, Advice
from django.core.exceptions import ObjectDoesNotExist



def index(request):
    question1 = Question.objects.get(pk=25)
    question2 = Question.objects.get(pk=19)
    question3 = Question.objects.get(pk=13)

    context = {'question1': question1, 'question2': question2, 'question3': question3 }
    return render(request, 'recsystem/index.html', context)

def details(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    followUps = FollowUp.objects.all()
    context = {
    'questions' : questions,
    'answers' : answers,
    'followUps' : followUps
    }
    return render(request, 'recsystem/questions.html', context)

def detail(request, question_id):
    return HttpResponse("<h2>Deatils for the question: " + str(question_id) + "</h2>")

def followUp(request):
    fid = request.GET['fid']
    # adviceId = request.GET['adviceId']
    advice = Advice.objects.filter(answer_labels=fid)

    try:
        fup = FollowUp.objects.get(answer=fid)
        Question = fup.question
        answers = Question.answer_set.all()
        context = {
        'question': serializers.serialize('python', [fup.question])[0],
        'answers' : serializers.serialize('python', answers),
        'advice' : serializers.serialize('python', advice)
        }

    except FollowUp.DoesNotExist:
        context = {
        'advice' : serializers.serialize('python', advice)
        }





    return JsonResponse(context, safe=False)


def add_question(request):

    form = QuestionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.save()
        return render(request, 'recsystem/questions.html', {'questions': Question.objects.all(), 'answers': Answer.objects.all(),
        'followUps': FollowUp.objects.all() })
    context = {
        "form": form,
    }
    return render(request, 'recsystem/add_question.html', context)

def add_answer(request):

    form = AnswerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.save()
        return render(request, 'recsystem/questions.html', {'questions': Question.objects.all() })
    context = {
        "form": form,
    }
    return render(request, 'recsystem/add_answer.html', context)

def add_relation(request):

    form = FollowUpForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        followUp = form.save(commit=False)
        followUp.save()
        return render(request, 'recsystem/questions.html', {'questions': Question.objects.all() })
    context = {
        "form": form,
    }
    return render(request, 'recsystem/add_relation.html', context)

def save_question(request):
    q = Question()
    q.question_title = request.POST['question_title']
    q.question_text = request.POST['question_text']
    q.extra_fields = request.POST['extraFields']
    q.save()
    return render(request, 'recsystem/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'recsystem/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                questions = Question.objects.all()
                return render(request, 'recsystem/index.html', {'questions': questions})
            else:
                return render(request, 'recsystem/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'recsystem/login.html', {'error_message': 'Invalid login'})
    return render(request, 'recsystem/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                questions = Question.objects.all()
                return render(request, 'recsystem/index.html', {'questions': questions})
    context = {
        "form": form,
    }
    return render(request, 'recsystem/register.html', context)
