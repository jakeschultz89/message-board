from django.db import models


class Post(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title[:50]
    