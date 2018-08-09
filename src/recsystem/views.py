from django.contrib.auth import authenticate, login
from django.core import serializers
from django.contrib.auth import logout
from django.http import HttpResponse
from django.utils import timezone
from django.http import JsonResponse
import logging
import itertools
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import  AdviceForm
from .models import Question, Answer, FollowUp, Advice
from django.core.exceptions import ObjectDoesNotExist



def index(request):

    return render(request, 'recsystem/index.html')

def studyrec(request):
    try:
        questions = Question.objects.filter(id__in=[175,179,190])
        context = {'questions': questions}
        return render(request, 'recsystem/recommender.html', context)
    except Question.DoesNotExist :
        raise ObjectDoesNotExist


def gitrec(request):
    try:
        questions = Question.objects.filter(id__in=[192,194,195,200,205])
        context = {'questions': questions}
        return render(request, 'recsystem/recommender.html', context)
    except Exception.DoesNotExist:
        raise ObjectDoesNotExist


def others(request):
    questions = Question.objects.filter(followUp=False).exclude(id__in=[175,179,190,192,194,195,200,205])
    context = {'questions': questions}
    return render(request, 'recsystem/recommender.html', context)

def question_form(request):
    questions = Question.objects.all()
    advices = Advice.objects.all()
    context = {
    'allQuestions': questions,
    'advices': advices,
    'allAdvices' : serializers.serialize('json', advices)
    }
    return render(request, 'recsystem/question_form.html', context)

def getAdvices(request):
    advices = Advice.objects.all()
    context = {
    'advices' : serializers.serialize('python', advices)
    }
    return JsonResponse(context, safe=False)

def allAdvices(request):
    advices = Advice.objects.all()
    context = {
    'advices' : advices
    }
    return render(request, 'recsystem/advices.html', context)

def details(request):
    questions = Question.objects.all()
    firstQuestions = Question.objects.filter(followUp=False)
    answers = Answer.objects.all()
    followUps = FollowUp.objects.all()
    advices = Advice.objects.all()
    context = {
    'questions' : questions,
    'answers' : answers,
    'followUps' : followUps,
    'firstQuestions' : firstQuestions,
    'advices' : advices
    }
    return render(request, 'recsystem/questions.html', context)

def editQuestion(request, question_id):
    questions = Question.objects.all()
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answer_set.all()
    allAdvices = Advice.objects.all()

    context = {
    'questions': questions,
    'question': question,
    'answers': answers,
    'allAdvices': allAdvices
    }
    return render(request, 'recsystem/editQuestion.html', context)


def editAdvice(request, advice_id):
    advice = get_object_or_404(Advice, pk=advice_id)
    context = {
    'advice' : advice
    }
    return render(request, 'recsystem/editAdvice.html', context)

def detail(request, question_id):
    return HttpResponse("<h2>Deatils for the question: " + str(question_id) + "</h2>")

def followUp(request):
    fid = request.GET['fid']
    selAns = Answer.objects.get(pk=fid)
    advices = selAns.advices.all()

    try:
        fup = FollowUp.objects.get(answer=fid)
        Question = fup.question
        answers = Question.answer_set.all()
        context = {
        'question': serializers.serialize('python', [fup.question])[0],
        'answers' : serializers.serialize('python', answers),
        'advices' : serializers.serialize('python', advices)
        }

    except FollowUp.DoesNotExist:
        context = {
        'advices' : serializers.serialize('python', advices)
        }

    return JsonResponse(context, safe=False)

def getAns(request):
    qid = request.GET['qid']
    question = Question.objects.get(pk=qid)
    answers =  question.answer_set.all()
    context = {
        'answers' : serializers.serialize('python', answers),
    }

    return JsonResponse(context, safe=False)

def getSliderAdvice(request):
    aid = request.GET['ansId']
    answer = Answer.objects.get(pk=aid)
    advices = answer.advices.all()
    context = {
    'advices' : serializers.serialize('python', advices)
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

def add_advice(request):

    form = AdviceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        advice = form.save(commit=False)
        advice.save()
        return render(request, 'recsystem/questions.html', {'questions': Question.objects.all() })
    context = {
        "form": form,
    }
    return render(request, 'recsystem/add_advice.html', context)

def add_relation(request):

    answers = Answer.objects.all()
    questions = Question.objects.all()

    context = {
    'answers' : answers,
    'questions' : questions
    }
    return render(request, 'recsystem/add_relation.html', context)

def save_relation(request):
    f = FollowUp()
    f.answer = Answer.objects.get(pk=request.POST.get('answer'))
    f.question = Question.objects.get(pk=request.POST.get('question'))
    f.save()
    return JsonResponse({'result':'ok'})

def saveAdvice(request, advice_id):

    advice = get_object_or_404(Advice, pk=advice_id)
    advice.advice_label = request.POST['advice_label']
    advice.advice_text = request.POST['advice_text']
    advice.time_stamp = timezone.now()
    advice.save()
    advices = Advice.objects.all()
    context = {
    'advices' : advices
    }
    return render(request, 'recsystem/advices.html', context)


def save_question(request):
    q = Question()
    q.question_title = request.POST['question_title']
    q.question_text = request.POST['question_text']
    q.extra_fields = request.POST['extraFields']
    q.save()
    return render(request, 'recsystem/index.html')

def saveData(request):

    if request.method =='POST' and request.is_ajax():
        q = Question()
        q.question_title = request.POST['queTitle']
        q.question_text = request.POST['queText']
        q.description = request.POST['desc']
        q.options_type = request.POST['optionType']
        q.save()

        if request.POST.get('ansId'):
            try:
                followup = FollowUp()
                q.followUp = True
                q.save()
                followup.description = ""
                followup.answer = Answer.objects.get(pk=request.POST['ansId'])
                followup.question = q
                followup.save()

            except :
                pass

        if request.POST.getlist('anstextArray[]'):
            answers = request.POST.getlist('anstextArray[]')
            if request.POST.getlist('ansAdvicesArray[]'):
                advices = request.POST.getlist('ansAdvicesArray[]')
                zippedList = zip(answers, advices)
                for an, ad in zippedList:
                    adviceList = str(ad)
                    adviceList = adviceList.split(',')
                    answer = Answer()
                    answer.question = q
                    answer.answer_text = an
                    answer.save()
                    for item in adviceList:
                        advice = get_object_or_404(Advice, pk=int(item))
                        answer.advices.add(advice)

                    answer.save()
            else:
                for item in answers:
                    answer = Answer()
                    answer.question = q
                    answer.answer_text = item
                    answer.save()
        elif request.POST.getlist('ansMinArray[]') and request.POST.getlist('ansMaxArray[]'):
            q.min = request.POST.get('minVal')
            q.max = request.POST.get('maxVal')
            q.step = request.POST.get('step')
            q.save()
            minList = request.POST.getlist('ansMinArray[]')
            maxList = request.POST.getlist('ansMaxArray[]')
            if request.POST.getlist('ansAdvicesArray[]'):
                advices = request.POST.getlist('ansAdvicesArray[]')
                zip_min_max_ad = zip(minList, maxList, advices)
                for min, max, ad in zip_min_max_ad:
                    adviceList = str(ad)
                    adviceList = adviceList.split(',')
                    answer = Answer()
                    answer.question = q
                    answer.min_val = min
                    answer.max_val = max
                    answer.save()
                    for item in adviceList:
                        advice = get_object_or_404(Advice, pk=int(item))
                        answer.advices.add(advice)
                        answer.save()
            else:
                zip_min_max = zip(minList, maxList)
                for min, max in zip_min_max:
                    answer = Answer()
                    answer.question = q
                    answer.min_val = min
                    answer.max_val = max
                    answer.save()


        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'nok'})

def saveEditedData(request):
    if request.method =='POST' and request.is_ajax():
        q = Question.objects.get(pk=request.POST['queId'])
        q.question_title = request.POST['queTitle']
        q.question_text = request.POST['queText']
        q.description = request.POST['desc']
        q.options_type = request.POST['optionType']
        q.save()

        if request.POST.get('ansId'):
            try:
                followup = FollowUp()
                q.followUp = True
                q.save()
                followup.description = ""
                followup.answer = Answer.objects.get(pk=request.POST['ansId'])
                followup.question = q
                followup.save()

            except :
                pass

        if request.POST.getlist('anstextArray[]'):
            answers = request.POST.getlist('anstextArray[]')
            ansIds = request.POST.getlist('ansIdArray[]')
            if request.POST.getlist('ansAdvicesArray[]'):
                advices = request.POST.getlist('ansAdvicesArray[]')
                zippedList = zip(ansIds, answers, advices)
                for ai, an, ad in zippedList:
                    adviceList = str(ad)
                    adviceList = adviceList.split(',')
                    answer = get_object_or_404(Answer, pk=ai)
                    answer.answer_text = an
                    answer.save()
                    for item in adviceList:
                        advice = get_object_or_404(Advice, pk=int(item))
                        answer.advices.add(advice)

                    answer.save()
            else:
                zippedList = zip(ansIds, answers)
                for ai, an in zippedList:
                    answer = get_object_or_404(Answer, pk=ai)
                    answer.answer_text = an
                    answer.save()
        elif request.POST.getlist('ansMinArray[]') and request.POST.getlist('ansMaxArray[]'):
            minList = request.POST.getlist('ansMinArray[]')
            maxList = request.POST.getlist('ansMaxArray[]')
            ansIds = request.POST.getlist('ansIdArray[]')
            if request.POST.getlist('ansAdvicesArray[]'):
                advices = request.POST.getlist('ansAdvicesArray[]')
                zip_min_max_ad = zip(minList, maxList, ansIds, advices)
                for min, max, ai, ad in zip_min_max_ad:
                    adviceList = str(ad)
                    adviceList = adviceList.split(',')
                    answer = get_object_or_404(Answer, pk=ai)
                    answer.min_val = min
                    answer.max_val = max
                    answer.save()
                    for item in adviceList:
                        advice = get_object_or_404(Advice, pk=int(item))
                        answer.advices.add(advice)

                    answer.save()
            else:
                zip_min_max_ai = zip(minList, maxList, ansIds)
                for min, max, ai in zip_min_max_ai:
                    answer = get_object_or_404(Answer, pk=ai)
                    answer.min_val = min
                    answer.max_val = max
                    answer.save()

        return JsonResponse({'result':'ok'})
    else:
        return JsonResponse({'result':'nok'})

def delete(request, question_id):
    question = Question.objects.get(pk=question_id)
    question.delete()
    questions = Question.objects.all()

    return render(request, 'recsystem/questions.html', {'questions': questions} )

def deleteAll(request):

    Question.objects.all().delete()
    Answer.objects.all().delete()
    FollowUp.objects.all().delete()
    Advice.objects.all().delete()

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
