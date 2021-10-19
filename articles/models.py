from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    publish = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True,)

    def __str__(self):
        return self.title
