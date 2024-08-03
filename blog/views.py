from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
class BlogListView(ListView):
    """Контроллер просмотра списка постов"""
    model = Post
    ordering = '-created_at'


class BlogDetailView(DetailView):
    """Контроллер просмотра отдельного поста"""
    model = Post

    def get_object(self, queryset=None):
        """Счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
