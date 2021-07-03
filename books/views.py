from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Author, Book, Review


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'books/detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context_dict = {
        'books': books,
    }
    return render(request, 'books/author_books.html', context_dict)

def review(request, id):
    body = request.POST['review']
    new_review = Review(body=body, book_id=id)
    new_review.save()
    return redirect('home')


