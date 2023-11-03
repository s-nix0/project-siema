from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.author) + ' | ' + str(self.title) + ' | ' + str(self.detail)


class Material(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.TextField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return str(self.pk) + ' | ' + str(self.author) + ' | ' + str(self.title) + ' | ' + str(self.detail)
