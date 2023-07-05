from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app1.models import Question

# def index(request):
#     return HttpResponse("Hello, world! From app1")

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', </br>'.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app1/index.html', context)