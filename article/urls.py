from django.urls import path
from .views import home


app_name="article"
urlpatterns=[
    path("",home,name="home"),
    path("page/<int:page>",home,name="home"),
]