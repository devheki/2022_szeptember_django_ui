from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# 'author': 'Ricsi Kovács',
# 'title': 'Blog post 1',
# 'content': 'First content',
# 'date_posted': '2022. szeptember 14',

class PostsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts'

    def __str__(self):
        return f"{self.title} - {self.author}"

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk": self.pk})