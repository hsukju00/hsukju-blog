from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    post_list = Post.objects.order_by('-published_at')[:5]
    context = {"post_list": post_list}
    return render(request, "blog/main.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "blog/post_detail.html", context)


def info(request):
    return render(request, "blog/info.html")
