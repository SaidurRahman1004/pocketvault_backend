from django.db import models
from django.contrib.auth.models import User
#Shopping Models Database
class ShoppingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    isBought = models.BooleanField(default=False)

    def __str__(self):
        return self.name

#Bookmark Models Database
class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.URLField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
#MediaItem Models Database
class MediaItem(models.Model):
    # Media Types Choices Like Enum
    class MediaType(models.TextChoices):
        MOVIE = 'MOVIE', 'Movie'
        BOOK = 'BOOK', 'Book'
        SERIES = 'SERIES', 'Series'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=MediaType.choices)
    status = models.CharField(max_length=100, default= 'Plan to Watch')
    rating = models.PositiveIntegerField(default=0)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title





