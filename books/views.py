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
    context_dict = {
        'books': data,
        'id': id
    }
    return render(request, 'books/detail.html', context_dict)
