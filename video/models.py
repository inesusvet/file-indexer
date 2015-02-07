# ~*~ coding: utf-8 ~*~
from django.db import models

from taggit.managers import TaggableManager
FILE_PATH_MAX_LENGTH = 1024


class Source(models.Model):
    path = models.CharField(u'Путь к директории', max_length=FILE_PATH_MAX_LENGTH)

    class Meta:
        verbose_name = u'Путь для поиска файлов'
        verbose_name_plural = u'Пути для поиска файлов'


class Video(models.Model):
    source = models.ForeignKey(Source, verbose_name=u'Где файл был найден')
    filename = models.FilePathField(u'Путь к файлу', max_length=FILE_PATH_MAX_LENGTH)
    tags = TaggableManager(u'Теги для поиска')

    fstat = models.CharField(u'Серилизованая информация о файле', max_length=200)

    class Meta:
        verbose_name = u'Видео-файл'
        verbose_name_plural = u'Видео-файлы'


__all__ = (
    'Source',
    'Video',
)
