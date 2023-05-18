from django.urls import path, include
import blog.views as views

app_name = "blog"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("category/", view=views.category_list, name="category"),
    path("tag/", view=views.tag_list, name="tag"),
    path("post/", view=views.post_list, name="post"),
    path("info/", view=views.info, name="info"),
]
