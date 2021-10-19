from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
