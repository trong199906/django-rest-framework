from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='api_overview'),
    path('BookList', views.BookList, name='book_list'),
    path('BookCreate', views.BookCreate, name='book_create'),
    path('BookUpdate', views.BookUpdate, name='book_update'),
    path('BookDelete', views.BookDelete, name='book_delete')
]