from django.db import models

# Create your models here.
class ToDo(models.Model):

    text = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BooksShop(models.Model):

    title = models.CharField(verbose_name ='Название книги',max_length = 100)
    subtitle = models.CharField(verbose_name ='Альтернативное название',max_length = 100)
    description = models.CharField(verbose_name ='Описание книги',max_length = 500)
    price = models.DecimalField(decimal_places=2,verbose_name='Цена',max_digits=10)
    genre = models.CharField(verbose_name ='Жанр книги',max_length = 200)
    author = models.CharField(verbose_name ='Автор книги',max_length = 100)
    year = models.DateField(verbose_name='Год выхода книги')
    date = models.DateTimeField(auto_now_add = True)
