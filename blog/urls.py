from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import BlogListView, BlogDetailView

urlpatterns = [
    path('', cache_page(60)(BlogListView.as_view()), name='index'),
    path('post/<int:pk>', cache_page(60)(BlogDetailView.as_view()), name='post'),
]
