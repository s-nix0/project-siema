from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user
from django.utils import timezone


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # other fields
#
#     def update_last_activity(self, act_type, act_level):
#         self.user.useractivity_set.create(
#             activity_type=act_type,
#             activity_level=act_level  # You may need to adjust this based on your logic
#         )
#         UserActivity.objects.create(
#             user=self.user,
#             activity_type=act_type,
#             activity_level=act_level
#         )


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_activity = models.DateTimeField(default=timezone.now)
    activity_title = models.TextField(null=True)
    activity_type = models.CharField(max_length=50, null=True)  # Add a type field
    activity_level = models.IntegerField(null=True)  # Add a level field

    def __str__(self):
        return f"{self.user.username} | {self.activity_type} | {self.activity_title} | {self.activity_level} | {self.last_activity}"

    class Meta:
        ordering = ['-last_activity']


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default='Post', max_length=255, editable=False)
    level = models.IntegerField(default=1, unique=True)
    detail = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    thumbnail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} | {self.author} | {self.title} | {self.detail}"


class Material(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default='Materi', max_length=255, editable=False)
    level = models.IntegerField(default=1, unique=True)
    detail = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    thumbnail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} | {self.author} | Materi = {self.level} | {self.title} | {self.detail}"

    def get_absolute_url(self):
        return reverse('material-detail', args=[str(self.level)])


class Comic(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default='Komik', max_length=255, editable=False)
    level = models.IntegerField(default=1, unique=True)
    detail = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    thumbnail = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.pk} | {self.author} | Bagian = {self.level} | {self.title} | {self.detail}"

    def get_absolute_url(self):
        return reverse('comic-detail', args=[str(self.level)])


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default='Quiz', max_length=255, editable=False)
    level = models.IntegerField(default=1, unique=True)
    detail = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    thumbnail = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pk} | {self.author} | Level = {self.level} | {self.title} | {self.detail}"

    def get_absolute_url(self):
        return reverse('quiz-detail', args=[str(self.level)])
