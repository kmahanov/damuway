from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Recipe, Comment, Rating
from .forms import CommentForm, RatingForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    age_group = request.GET.get('age_group')

    if age_group:
        recipes = recipes.filter(age_group=age_group)

    context = {
        'recipes': recipes,
        'age_groups': Recipe.AGE_GROUPS,
    }
    return render(request, 'recipes/recipe_list.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comments.all()


    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(recipe=recipe, user=request.user).first()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.recipe = recipe
                comment.user = request.user
                comment.save()
                messages.success(request, 'Комментарий добавлен!')
                return redirect('recipe_detail', pk=pk)

        elif 'rating_submit' in request.POST and request.user.is_authenticated:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                rating, created = Rating.objects.update_or_create(
                    recipe=recipe,
                    user=request.user,
                    defaults={'value': rating_form.cleaned_data['value']}
                )
                # Обновляем средний рейтинг рецепта
                recipe.average_rating = recipe.ratings.aggregate(models.Avg('value'))['value__avg'] or 0
                recipe.save()
                messages.success(request, 'Оценка сохранена!')
                return redirect('recipe_detail', pk=pk)
    else:
        comment_form = CommentForm()
        rating_form = RatingForm(initial={'value': user_rating.value} if user_rating else None)

    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'user_rating': user_rating,
    }
    return render(request, 'recipes/recipe_detail.html', context)