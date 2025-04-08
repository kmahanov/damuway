from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Question, AnswerOption


class SurveyView(View):
    def get(self, request, question_id=None):
        if not question_id:
            first_question = Question.objects.order_by('order').first()
            if first_question:
                return redirect('survey:question', question_id=first_question.id)
            return render(request, 'survey/complete.html')

        question = get_object_or_404(Question, id=question_id)
        next_question = Question.objects.filter(order__gt=question.order).order_by('order').first()

        return render(request, 'survey/question.html', {
            'question': question,
            'next_question_id': next_question.id if next_question else None,
            'progress': f"{question.order}/{Question.objects.count()}"
        })

    def post(self, request, question_id):
        answer_id = request.POST.get('answer_id')
        answer = get_object_or_404(AnswerOption, id=answer_id)
        next_question = Question.objects.filter(order__gt=answer.question.order).order_by('order').first()

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'feedback': answer.feedback,
                'next_question_id': next_question.id if next_question else None,
                'finished': not bool(next_question)
            })

        if next_question:
            return redirect('survey:question', question_id=next_question.id)
        return redirect('survey:complete')


class CompleteView(View):
    def get(self, request):
        return render(request, 'survey/complete.html')
