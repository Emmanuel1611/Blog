from django.db import models

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
