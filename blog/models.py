from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(default="")
    date = models.DateField()

    def __str__(self):
        return self.title
