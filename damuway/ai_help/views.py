# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import QuestionAnswer
# from .ai_generator import generate_answer
# from django.views.decorators.http import require_GET
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
#
# @login_required
# def ask_ai_view(request):
#     if request.method == "POST":
#         question = request.POST.get("question")
#         answer = generate_answer(question)
#
#         QuestionAnswer.objects.create(user=request.user, question=question, answer=answer)
#         return JsonResponse({"answer": answer})
#
#     history = QuestionAnswer.objects.filter(user=request.user).order_by('-created_at')[:5]
#     return render(request, 'ai_helper/ask.html', {'history': history})
#
#
#
# @login_required
# @require_GET
# def clear_history(request):
#     QuestionAnswer.objects.filter(user=request.user).delete()
#     return HttpResponse("OK")