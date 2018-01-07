from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    introduction = models.CharField(max_length=300)
    body = models.TextField()
    URL = models.URLField(blank=True, null=True)
    date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
