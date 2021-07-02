from django.shortcuts import render, redirect
from django.views import generic


from .models import Book, Review


class IndexView(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'books/detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


def review(request, id):
    body = request.POST['review']
    new_review = Review(body=body, book_id=id)
    new_review.save()
    return redirect('home')
