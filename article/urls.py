from django.urls import path
from .views import (
    home,
    teams_article,
    accept,
    reject,
    request,
    article,
    register_newsletter,
    Create_Article,
    Update_Article,
    Delete_Article,
    )


app_name="article"
urlpatterns=[
    path("",home,name="home"),
    path("page/<int:page>/",home,name="home"),
    path("article/<int:article_id>/",article,name="article"),
    path("newsletter/register/",register_newsletter,name="newsletter"),
    path("teams/",teams_article,name="teams"),
    path("teams/page/<int:page>/",teams_article,name="teams"),
    path("article/<int:article_id>/accept/<username>/",accept,name="accept"),
    path("article/<int:article_id>/reject/<username>/",reject,name="reject"),
    path("article/<int:article_id>/request/",request,name="request"),
    path("article/create/",Create_Article.as_view(),name="create"),
    path("article/edit/<int:pk>/",Update_Article.as_view(),name="edit"),
    path("article/delete/<int:pk>/",Delete_Article.as_view(),name="delete"),
]