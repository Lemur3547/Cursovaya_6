from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Регистрация модели поста в админке"""
    fields = ('name', 'body', 'image')
    list_display = ('name', 'body',)
