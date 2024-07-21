from django.db import models
from django.conf import settings


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('MH', 'Mental Health'),
        ('HD', 'Heart Disease'),
        ('CV', 'Covid19'),
        ('IM', 'Immunization'),
    ]

    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.get_name_display()


class BlogPost(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
