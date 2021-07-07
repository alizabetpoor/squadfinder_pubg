from django.urls import path
from .views import account_profile,Signup,Login,home,logout_view,profile,acc_detail_view,edit_user_detail

app_name="user"
urlpatterns=[
    path("",home,name="home"),
    path("signup/",Signup,name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("acc_detail/",acc_detail_view,name="acc_detail"),
    path("profile/<str:username>",account_profile,name="account_profile"),
    path("detail/",edit_user_detail.as_view(),name="user_detail"),
]