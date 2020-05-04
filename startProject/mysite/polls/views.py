from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from polls.models import Question
from django.template import loader
from django.urls import reverse
from django.views import generic

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     return HttpResponse('''
#         <h1>Hello, world. You're at the polls index.</h1>
#         <h2>Hello, world. You're at the polls index.</h2>
#         <h3>Hello, world. You're at the polls index.</h3>
#         <h4>Hello, world. You're at the polls index.</h4>
#         <h5>Hello, world. You're at the polls index.</h5>
#         <h6>Hello, world. You're at the polls index.</h6>
#         <p>Hello, world. You're at the polls index.</p>
#      ''')

# def index(request):
#     import os 
#     print(os.getcwd())
#     with open('polls/templates/polls/index.html', 'r') as f:
#         file_text = f.read()
#     return HttpResponse(file_text)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = '<br> '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#         'username': 'Superman'
#     }
#     return HttpResponse(template.render(context, request))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         'latest_question_list': latest_question_list,
#         'username': 'Superman'
#     }
#     return render(request, 'polls/index.html', context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # queryset = Question.objects.order_by('-pub_date')[:5]
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    # def get_template_names(self):
    #     return 'polls/index.html'


# def detail(request, question_id):
#     # return HttpResponse("You're looking at question %s." % question_id)
#     return HttpResponse("You're looking at question {}.".format(question_id))

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
    
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
        
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/result.html', {'question': question})

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))