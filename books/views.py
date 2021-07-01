from django.shortcuts import render,  get_object_or_404, redirect
from django.views import generic


from .models import Book, Review


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


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
