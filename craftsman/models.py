from django.db import models
from autoslug import AutoSlugField


class Artist(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='Художник')
    slug = AutoSlugField(populate_from='full_name', unique=True)

    def __str__(self):
        return self.full_name


class Painting(models.Model):
    paint = models.CharField(max_length=255, verbose_name='Картина')
    category = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    text = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='paint/', verbose_name='Картина')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paint
