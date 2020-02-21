from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
