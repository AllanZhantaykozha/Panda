from distutils.command.upload import upload
from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField(max_length=150)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='categories')
    price = models.FloatField(default=0)
    photo = models.ImageField(upload_to='photo/%Y/%m%d')
    slug = models.SlugField(max_length=70, unique=True, db_index=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(max_length=70, unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']