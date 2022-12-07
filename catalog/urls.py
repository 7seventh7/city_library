from django.urls import path, include
from django.urls import include
from .views import *
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('books', BookListView.as_view(), name="all_books_list"),
    path('books_list', views.BookListView.as_view(), name='books'),
    path('book_detail/<int:book_id>/', get_single_page, name='book_detail'),
    path('authors', views.AuthorListView.as_view(), name="all_authors_list"),
    path('author_books/<int:author_id>/', get_all_author_books, name="author_books"),
    path('add_book', add_book, name="add_book"),
    path('contact_form', contact_form, name="contact_form"),
    path('login2', LoginUser.as_view(), name="login2"),
    path('logout2', logout_user, name="logout2"),
    path('registration', RegisterUser.as_view(), name="registration"),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
