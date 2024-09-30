from rest_framework import serializers
from .models import Abonent, Book, Genre, Author

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author 
        fields = ('pk', 'name')

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre 
        fields = ('pk', 'title')

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book 
        fields = ('pk', 'title', 'description', 'content', 'author', 'genre')

class AbonentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Abonent 
        fields = ('pk', 'user', 'book')
        

