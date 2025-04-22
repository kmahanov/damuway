from django.shortcuts import render, get_object_or_404
from .models import ChildDevelopment, DevelopmentComment

def development_list(request):
    developments = ChildDevelopment.objects.all()
    return render(request, 'child/development_list.html', {'developments': developments})

def development_detail(request, age):
    development = get_object_or_404(ChildDevelopment, age=age)
    comments = development.comments.all()

    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('text')
        if text:
            DevelopmentComment.objects.create(
                development=development,
                user=request.user,
                text=text
            )

    return render(request, 'child/development_detail.html', {
        'development': development,
        'comments': comments
    })
