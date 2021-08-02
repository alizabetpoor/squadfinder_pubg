from django.urls import path
from .forms import emailvalidatepasswordreset
from .views import (
setting,
account_profile,
Signup,
Login,
home,
logout_view,
profile,
acc_detail_view,
passwordreset,
passwordresetdone,
passwordresetcomplete,
passwordresetconfrim,
)

app_name="user"
urlpatterns=[
    path("",home,name="home"),
    path("signup/",Signup,name="signup"),
    path("login/",Login.as_view(),name="login"),
    path("logout/",logout_view,name="logout"),
    path("acc_detail/",acc_detail_view,name="acc_detail"),
    path("profile/<str:username>",account_profile,name="account_profile"),
    path("setting/",setting,name="user_setting"),
    path("reset_password/",passwordreset.as_view(),name="reset_password"),
    path("reset/<uidb64>/<token>/",passwordresetconfrim.as_view(),name="reset_password_confrim"),
    path("reset/done/",passwordresetcomplete.as_view(),name="reset_password_complete"),
    path("reset_password/done/",passwordresetdone.as_view(),name="reset_password_done"),
]