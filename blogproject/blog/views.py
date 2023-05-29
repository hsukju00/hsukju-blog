from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Post


def index(request):
    posts = Post.objects.order_by('-published_at')
    paginator = Paginator(posts, 5)
    posts_in_page = paginator.get_page(1)
    context = {"posts": posts_in_page}
    return render(request, "blog/main.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {post: post}
    return render(request, "blog/post_detail.html", context)


def info(request):
    return render(request, "blog/info.html")
