# Generated by Django 3.1.4 on 2021-01-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('subtitle', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('genre', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('year', models.DateField(verbose_name='Год выхода книги')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]