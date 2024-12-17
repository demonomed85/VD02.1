from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)
    short_description = models.CharField('Краткое описание новости', max_length=200)
    full_description = models.TextField('Полное описание новости')
    author = models.TextField('Автор', max_length=50)
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
