from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

from django_sorcery.shortcuts import get_object_or_404

from .models import Question, Choice, db


def index(request):
    latest_question_list = Question.objects.order_by(
        Question.pub_date.desc())[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    selected_choice = Choice.query.filter(
        Choice.question == question,
        Choice.pk == request.POST['choice'],
    ).one_or_none()

    if not selected_choice:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    selected_choice.votes += 1
    db.flush()
    return HttpResponseRedirect(reverse('polls:results', args=(question.pk,)))
