from django.urls import path, include
import blog.views as views

app_name = "blog"

urlpatterns = [
    path("", view=views.index, name="index"),
    path("info/", view=views.info, name="info"),

    path("post/<int:post_id>", view=views.post_detail, name="post"),
]
