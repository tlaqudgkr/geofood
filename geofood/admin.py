from django.contrib import admin
from geofood.models import Restaurant, Category, Post


class Categorylist(admin.ModelAdmin):
    list_display = ('groop', 'name')


# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Category, Categorylist)
admin.site.register(Post)