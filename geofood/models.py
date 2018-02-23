from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    groop = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    zoom = models.PositiveSmallIntegerField(default=14)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    author = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Restaurant)
    # 카테고리가 free인 경우 : 등록대기
    category = models.ForeignKey(Category, null=True, blank=True)

    def __str__(self):
        return self.text[:50]
