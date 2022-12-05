from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import Book, Author, BookInstance, Genre
from random import randint
from django.views import generic

# def index(request):
#
#     return HttpResponse(print(request.headers))


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


def all_books_list(request):
    """
    Функция отображения всех существующих книг в библиотеке
    :param request:
    :return:
    """
    books_title = Book.objects.all()



    return render(
        request,
        'catalog/all_books_list.html',
        context={'books_title': books_title,},
    )

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
        context={'books': books,},
    )

def add_book(request):
    form = AddBookForm()
    return render(
        request,
        'catalog/add_book.html',
        context={'title': 'Добавление статьи' , 'form': form},
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
        context={'title': 'Добавление статьи' , 'form': form},
    )



class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book

# class AutorListView(generic.ListView):
#     model = Author

def login2(request):
    data = request.META.get("HTTP_REFERER")
    return render(request,
            "catalog/login2.html", {"data": data,})

# def registration2(request):
#     data = request.__dict__
#     return render(request,
#             "catalog/registration.html", {"data": data,})



class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'catalog/registration.html'
    success_url = reverse_lazy('login2')
