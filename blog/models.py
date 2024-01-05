from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField

def validate_title_characters(value):
    validate_only_characters(value, 'title')

def validate_only_characters(value, field_name):
    if not value.isalpha():
        raise ValidationError(f'Only characters are allowed in the {field_name} field.')
    
class Blog(models.Model):
    title = models.CharField(max_length=255, validators=[validate_title_characters])
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
