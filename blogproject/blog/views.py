from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog/main.html")


from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, template_name="blog/main.html")


def category_list(request):
    return render(request, template_name="blog/category.html")


def tag_list(request):
    return render(request, template_name="blog/tag_list.html")


def post_list(request):
    return render(request, template_name="blog/post.html")


def info(request):
    return render(request, template_name="blog/info.html")
