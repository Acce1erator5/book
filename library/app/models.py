from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    quantity = models.IntegerField()
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.year} - {self.quantity} - {self.author} - {self.genre} "

