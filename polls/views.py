from django.http import HttpResponse
from django.shortcuts import render
from . import models

def index(request):
    latest_question_list = models.Question.objects.order_by('-pub_date')[:5]
    context = {
            'latest_question_list': latest_question_list,
            }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on qustion {question_id}")
