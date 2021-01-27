# Generated by Django 3.1.4 on 2021-01-27 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_booksshop'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksshop',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booksshop',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор книги'),
        ),
        migrations.AlterField(
            model_name='booksshop',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Описание книги'),
        ),
        migrations.AlterField(
            model_name='booksshop',
            name='genre',
            field=models.CharField(max_length=200, verbose_name='Жанр книги'),
        ),
        migrations.AlterField(
            model_name='booksshop',
            name='subtitle',
            field=models.CharField(max_length=100, verbose_name='Альтернативное название'),
        ),
    ]