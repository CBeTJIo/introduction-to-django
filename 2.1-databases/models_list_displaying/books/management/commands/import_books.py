import json
from django.core.management.base import BaseCommand
from books.models import Book
from django.template.defaultfilters import slugify

class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('books.json', encoding='utf-8') as f:
            books = json.load(f)

        for book in books:
            new_book = Book(
                name=book.get('fields').get('name'),
                author=book.get('fields').get('author'),
                pub_date=book.get('fields').get('pub_date'),
            )
            new_book.save()