from django.shortcuts import render, get_object_or_404, redirect
from .models import ChildDevelopment, DevelopmentComment
from .forms import CommentForm

def development_list(request):
    developments = ChildDevelopment.objects.all()
    return render(request, "development/list.html", {"developments": developments})

def development_detail(request, age):
    development = get_object_or_404(ChildDevelopment, age=age)
    comments = development.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.development = development
            comment.save()
            return redirect("development_detail", age=age)
    else:
        form = CommentForm()

    return render(request, "development/development_detail.html", {
        "development": development,
        "comments": comments,
        "form": form
    })
