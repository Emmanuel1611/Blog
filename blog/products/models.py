from django.db import models
from blog.models import Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    affiliate_link = models.URLField()
    image = models.URLField()
    rating = models.FloatField(default=0.0)  # e.g., 4.5
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 99.99
    categories = models.ManyToManyField(Category, related_name='products')
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name