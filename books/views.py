from django.shortcuts import render


from .models import Book


def index(request):

    data = Book.objects.all()

    context_dict = {
        'books': data
    }
    return render(request, 'books/index.html', context_dict)


def detail(request, id):
    single_book = Book.objects.get(pk=id)

    context_dict = {
        'book': single_book
    }
    return render(request, 'books/detail.html', context_dict)
