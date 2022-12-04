from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views.generic import ListView

from .forms import *
from .models import Book, Author, BookInstance, Genre
from random import randint
from django.views import generic
from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применён по умолчанию.

    latest_object = Book.objects.all().reverse()[0]
    count = Book.objects.count()
    random_object = Book.objects.all()[randint(0, count - 1)]
    while (latest_object == random_object):
        random_object = Book.objects.all()[randint(0, count - 1)]

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'catalog/index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available,
                 'num_authors': num_authors, 'random_object': random_object, 'latest_object': latest_object,
                 'num_visits': num_visits},
    )


# def all_books_list(request):
#     """
#     Функция отображения всех существующих книг в библиотеке
#     """
#     books_title = Book.objects.all()
#
#     return render(
#         request,
#         'catalog/all_books_list.html',
#         context={'books_title': books_title, },
#     )


def all_authors(request):
    authors = Author.objects.all()

    return render(
        request,
        'catalog/authors_list.html',
        context={'authors': authors, },
    )


def get_single_page(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404("Такой книги не существует")

    return render(
        request,
        'catalog/book_page.html',
        context={'book': book, },
    )

def get_all_author_books(request, author_id):
    try:
        books = Book.objects.filter(author_id=author_id)
    except Book.DoesNotExist:
        raise Http404("Такого автора нету")

    return render(
        request,
        'catalog/books_of_single_author.html',
        context={'books': books, },
    )


def add_book(
        request):  # Разобраться с багом!!! В форме нужно сразу мочь добавлять нового автора, а не выбирать из списка существующих
    # form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # перенаправляемся на главную страницу если форма заполненна корректно
    else:
        form = AddBookForm()
    return render(
        request,
        'catalog/add_book.html',
        context={'title': 'Добавление статьи', 'form': form},
    )


def contact_form(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     else:
    #         form = ContactForm()
    form = ContactForm()
    return render(
        request,
        'catalog/contact_form.html',
        context={'title': 'Форма для связи', 'form': form},
    )


class BookListView(ListView):
    model = Book
    template_name = 'catalog/all_books_list.html'
    context_object_name = 'books_title'


class BookDetailView(generic.DetailView):
    model = Book

# class AutorListView(generic.ListView):
#     model = Author
