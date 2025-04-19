from django.shortcuts import render, get_object_or_404
from .models import Book, Genre, Author, Quote, Review
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.shortcuts import redirect

def book_list(request):
    query = request.GET.get('q')
    genre_id = request.GET.get('genre')
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) | 
            Q(author__name__icontains=query)
        )

    if genre_id:
        books = books.filter(genre__id=genre_id)

    context = {
        'new_books': books.filter(is_new=True),
        'popular_books': books.filter(is_popular=True),
        'recommended_books': books.filter(is_recommended=True),
        'genres': Genre.objects.all(),
    }
    return render(request, 'book/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book/book_detail.html', {'book': book})

def quote_list(request, pk):
    book = get_object_or_404(Book, pk=pk)
    quotes = book.quotes.all()
    return render(request, 'book/quote_list.html', {'book': book, 'quotes': quotes})

@login_required
def add_review(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('book:book_detail', pk=book.pk)
    else:
        form = ReviewForm()

    return render(request, 'book/add_review.html', {'form': form, 'book': book})
