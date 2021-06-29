from django.http.response import HttpResponse
from django.shortcuts import render
import os
import json

from django_Bookstore.settings import BASE_DIR

book_data = open(os.path.join(
    BASE_DIR, 'books/static/books/assets/books.json')).read()
data = json.loads(book_data)


def index(request):

    context_dict = {
        'books': data
    }
    return render(request, 'books/index.html', context_dict)


def detail(request, id):
    single_book = ''

    for book in data:
        if book.get('id') == id:
            single_book = book

    context_dict = {
        'book': single_book
    }
    return render(request, 'books/detail.html', context_dict)
