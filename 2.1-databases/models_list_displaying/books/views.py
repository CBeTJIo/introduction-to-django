import os.path
from django.shortcuts import render
from books.models import Book
import json

with open('books.json', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    new_book = Book(
        name=book.get('fields').get('name'),
        author=book.get('fields').get('author'),
        pub_date=book.get('fields').get('pub_date'),
    )
    new_book.save()

def books_view(request):
    template = 'books_list.html'

    catalog_objects = Book.objects.all()

    list_book = []
    for book  in catalog_objects:
        new_dict = {
            'name': book.get('fields').get('name'),
            'author': book.get('fields').get('author'),
            'pub_date': book.get('fields').get('pub_date'),
        }
        list_book.append(new_dict)

    context = {
        'books': list_book
    }
    return render(request, template, context)

def book_view(request):
    template = 'books/books_list.html'
    context = {}
    return render(request, template, context)
