from django.contrib import admin

from blog.models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ('name', 'body', 'image')
    list_display = ('name', 'body',)
