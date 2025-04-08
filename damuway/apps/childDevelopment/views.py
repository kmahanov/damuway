from django.shortcuts import render, get_object_or_404, redirect
from .models import ChildDevelopment, DevelopmentComment
from django.contrib.auth.decorators import login_required
from .forms import DevelopmentCommentForm

def development_list(request):
    stages = ChildDevelopment.objects.all()
    return render(request, 'child/development_list.html', {'stages': stages})

def development_detail(request, pk):
    stage = get_object_or_404(ChildDevelopment, pk=pk)
    comments = stage.comments.all()
    return render(request, 'child/development_detail.html', {
        'stage': stage,
        'comments': comments
    })

@login_required
def add_comment(request, pk):
    stage = get_object_or_404(ChildDevelopment, pk=pk)
    if request.method == 'POST':
        form = DevelopmentCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.development = stage
            comment.save()
            return redirect('development_detail', pk=stage.pk)
    else:
        form = DevelopmentCommentForm()
    return render(request, 'child/add_comment.html', {'form': form})
