from django.urls import path
from article.views import user_articles
from .views import (
setting,
account_profile,
Signup,
Login,
logout_view,
passwordreset,
passwordresetdone,
passwordresetcomplete,
passwordresetconfrim,
home,
)

app_name="user"
urlpatterns=[
    path("",home,name="home"),
    path("signup/",Signup,name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("profile/<str:username>/",account_profile,name="account_profile"),
    path("setting/",setting,name="user_setting"),
    path("reset_password/",passwordreset.as_view(),name="reset_password"),
    path("reset/<uidb64>/<token>/",passwordresetconfrim.as_view(),name="reset_password_confrim"),
    path("reset/done/",passwordresetcomplete.as_view(),name="reset_password_complete"),
    path("reset_password/done/",passwordresetdone.as_view(),name="reset_password_done"),
    path("articles/",user_articles,name="articles"),
    path("articles/page/<int:page>/",user_articles,name="articles"),
]