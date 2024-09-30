from django.db import models
from django.conf import settings

class Author(models.Model):
    name = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name
    
class Genre(models.Model):
    title = models.CharField("Name", max_length=240)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField("Name", max_length=150)
    description = models.CharField("Name", max_length=240)
    content = models.CharField("URL", max_length=512)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

class Abonent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
