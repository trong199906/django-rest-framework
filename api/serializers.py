from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        Model = Book
        fields = ['id', 'title', 'description', 'created_at']


class AuthorSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        Model = Author
        fields = ['id', 'name', 'book']
