from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Article, Category, ArticleLike, Comment


def article_list(request):
    search = request.GET.get('search', '')
    category_id = request.GET.get('category')
    articles = Article.objects.all()

    if search:
        articles = articles.filter(title__icontains=search)
    if category_id:
        articles = articles.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles, 'categories': categories})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    related_articles = Article.objects.filter(category=article.category).exclude(pk=pk)[:4]

    if request.method == 'POST':
        author = request.POST.get('author')
        text = request.POST.get('text')
        if author and text:
            Comment.objects.create(article=article, author=author, text=text)

    comments = article.comments.all()
    return render(request, 'articles/article_detail.html', {
        'article': article,
        'related_articles': related_articles,
        'comments': comments,
    })


def like_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'Unauthorized'}, status=403)

    liked, created = ArticleLike.objects.get_or_create(article=article, user=user)
    if not created:
        liked.delete()
        liked_status = False
    else:
        liked_status = True

    return JsonResponse({'liked': liked_status, 'likes_count': article.likes.count()})
