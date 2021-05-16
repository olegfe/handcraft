"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


from datetime import datetime
from django.core.urlresolvers import reverse
# Create your models here.
# модель данных Блога

class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание" ,)
    posted = models.DateTimeField(default = datetime.now(),db_index = True, verbose_name = "Опубликована")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_urls(self): #метод возвращает строку с уникальным интернет адресом записи
        return reverse("blogpost", args=[str(self.id)])

    def __str__(self):
        return self.title # метод возвращает название используемое для представления отдельных заголовков
    
    class Meta:
        db_table = "Posts" # имя таблицы для модели
        ordering = ["-posted"] # порядок сортировки данных в модели (- означает по убыванию)
        verbose_name = "статья блога" # имя под окторым модель будет отображаться в админ разделе
        verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(),db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def __str__(self):
        return 'Комментарий %s к %s' %(self.author, self.post)

    class Meta:
        db_table = "Comments" # имя таблицы для модели
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering= ["-date"]

admin.site.register(Comment)