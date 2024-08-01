from django.views.generic import ListView, DetailView

from blog.models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    ordering = '-created_at'


class BlogDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
