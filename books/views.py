from django.shortcuts import render,  get_object_or_404, redirect


from .models import Book, Review


def index(request):

    data = Book.objects.all()

    context_dict = {
        'books': data
    }
    return render(request, 'books/index.html', context_dict)


def detail(request, id):
    single_book = get_object_or_404(Book, pk=id)
    reviews = Review.objects.filter(book_id=id).order_by('-created_at')

    context_dict = {
        'book': single_book,
        'reviews': reviews
    }
    return render(request, 'books/detail.html', context_dict)


def review(request, id):
    body = request.POST['review']
    new_review = Review(body=body, book_id=id)
    new_review.save()
    return redirect('home')
