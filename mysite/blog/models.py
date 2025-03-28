from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='Назва')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Опис')
    published_date = models.DateTimeField(auto_created=True, verbose_name='Дата та час публікації')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    photo = models.URLField(unique=True, verbose_name="Посилання", default=None)
    tag = models.ManyToManyField(Tag, related_name='Post', verbose_name="Тег")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


class Comment(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    comment = models.TextField(verbose_name='Комментар')
    published_date = models.DateTimeField(auto_created=True, verbose_name='Дата та час публікації')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Новина')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Комментар'
        verbose_name_plural = 'Комментарі'
