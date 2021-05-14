from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    urls = {
        'BookList': 'book_list',
        'BookCreate': 'book_create',
        'BookUpdate/<int: id>/': 'book_update',
        'BookDelete/<int : id>/': 'book_delete'
    }

    return Response(urls)


@api_view(['POST'])
def BookList(request):
    author = Author.objects.all()
    authorserializer = AuthorSerializer(author, many=True)
    return Response(authorserializer.data)


@api_view(['POST'])
def BookCreate(request):
    if request.user.is_authenicate():
        authorserializer = AuthorSerializer(data=request.data)
        if authorserializer.is_valid():
            authorserializer.save()
    else:
        return Response('please login and use it')
    return Response(authorserializer.data)


@api_view(['POST'])
def BookUpdate(request, id):
    if request.user.is_authenicate():
        author = Author.objects.get(id=id)
        Authorserializer = AuthorSerializer(instance=author, data=request.data)
        if Authorserializer.is_valid():
            Authorserializer.save()
    else:
        return Response('please login and use it')
    return Response(Authorserializer)


@api_view(['DELETE'])
def BookDelete(request, id):
    if request.user.is_authenicate():
        author = Author.objects.get(id=id)
        author.delete()
    else:
        return Response('please login and use it')
    return Response('deleted was deleteful')
