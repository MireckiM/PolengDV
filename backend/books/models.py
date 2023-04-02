from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    pages = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
