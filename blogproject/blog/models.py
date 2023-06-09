from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name="카테고리")
    upper_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="제목")
    content = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(null=True, blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name="태그")
    posts = models.ManyToManyField(Post)
