from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        #ordering = ['id']

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=40, verbose_name='Описание')
    scope = models.ManyToManyField(Article, related_name='scopes_tag', through='Relationship')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'



class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, blank=False, related_name='scopes', verbose_name='Раздел')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        db_table = 'articles_relationship'
        ordering = ['-is_main', 'tag__name']