from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
