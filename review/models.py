from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    year = models.IntegerField()


class Review(models.Model):
    comment = models.CharField(max_length=255)
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
