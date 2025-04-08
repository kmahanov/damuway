from django.shortcuts import render, redirect
from django.views import View
from .models import Question, AnswerOption, UserResponse
from django.http import JsonResponse


class SurveyView(View):
    def get(self, request):
        questions = Question.objects.order_by('order')
        return render(request, 'survey/survey.html', {'questions': questions})

    def post(self, request):
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key

        selected_answer_id = None
        for key, value in request.POST.items():
            if key.startswith('question_'):
                selected_answer_id = value
                question_id = key.split('_')[1]
                UserResponse.objects.create(
                    question_id=question_id,
                    answer_id=selected_answer_id,
                    session_key=session_key
                )

        if selected_answer_id:
            answer = AnswerOption.objects.get(id=selected_answer_id)
            feedback = answer.feedback
        else:
            feedback = "Спасибо за участие!"

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'feedback': feedback})

        return render(request, 'survey/feedback.html', {'feedback': feedback})


def survey_thanks(request):
    return render(request, 'survey/thanks.html')