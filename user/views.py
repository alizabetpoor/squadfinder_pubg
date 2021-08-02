from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse
from .models import User,account_detail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from .forms import signupfrom,loginform,acc_detail_form,user_detail_form,change_password,emailvalidatepasswordreset,notifform
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)

from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.views.decorators.http import require_POST
# Create your views here.


def Signup(request):
    if request.method=="POST":
        form=signupfrom(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            acc_detail=account_detail(player=user)
            messages.success(request,"اکانت شما ساخته شد")
            return redirect("user:login")
        else:
            form=form
    else:
        
        form=signupfrom()
    return render(request,"user/auth/signup.html",context={"form":form})


class Login(LoginView):
    template_name="user/auth/login.html"
    authentication_form=loginform
@login_required
def home(request):
    return render(request,"user/account/home.html")

def logout_view(request):
    logout(request)
    messages.success(request,"شما از اکانت خود خارج شدید.")
    return redirect("user:login")
def profile(request):
    return render(request,"user/account/base.html")


# class acc_detail_view(LoginRequiredMixin,UpdateView):
#     model=account_detail
#     template_name="user/account/acc_detail.html"
#     form_class=acc_detail_form
#     success_url=reverse_lazy("user:acc_detail")

#     def get_object(self):
#         return account_detail.objects.get_or_create(player__pk=self.request.user.pk)

def acc_detail_view(request):
    acc_detail=account_detail.objects.filter(player=request.user).first()
    if acc_detail:
        if request.method=="POST":
            form=acc_detail_form(request.POST,instance=acc_detail)
            if form.is_valid():
                print("sa")
                acc_detail=form.save(commit=False)
                acc_detail.player=request.user
                acc_detail.save()

        else:
            form=acc_detail_form(instance=acc_detail)

    else:
        if request.method=="POST":
            form=acc_detail_form(request.POST)
            if form.is_valid():
                acc_detail=form.save(commit=False)
                acc_detail.player=request.user
                acc_detail.save()
        else:
            form=acc_detail_form()

    context={"form":form}
    return render(request,"user/account/acc_detail.html",context=context)

# class edit_user_detail(LoginRequiredMixin,UpdateView):
#     model=User
#     template_name="user/account/user_detail.html"
#     form_class=user_detail_form
#     success_url=reverse_lazy("user:user_detail")
#     def get_object(self):
#         return User.objects.get(pk=self.request.user.pk)

def account_profile(request,username):
    user=get_object_or_404(User,username=username)
    context={"pk_user":user}
    return render(request,"user/account/profile.html",context=context)

@login_required
def setting(request):
    if request.method=="POST":
        acc_detail=account_detail.objects.filter(player=request.user).first()
        if  "update_profile" in  request.POST:
            form_user_detail=user_detail_form(request.POST,instance=request.user)
            if form_user_detail.is_valid():
                form_user_detail.save()
            if acc_detail:
                form_account_detail=acc_detail_form(instance=acc_detail)
            else:
                form_account_detail=acc_detail_form()
            form_change_pass=change_password(request.user)
            form_notif=notifform(instance=request.user)
        elif "update_account" in request.POST:
            if acc_detail:
                form_account_detail=acc_detail_form(request.POST,instance=acc_detail)
                if form_account_detail.is_valid():
                    acc_detail=form_account_detail.save(commit=False)
                    acc_detail.player=request.user
                    acc_detail.save()


            else:
                form_account_detail=acc_detail_form(request.POST)
                if form_account_detail.is_valid():
                    acc_detail=form_account_detail.save(commit=False)
                    acc_detail.player=request.user
                    acc_detail.save()
            form_user_detail=user_detail_form(instance=request.user)
            form_change_pass=change_password(request.user)
            form_notif=notifform(instance=request.user)
        elif "update_password" in request.POST:
            form_change_pass=change_password(request.user,request.POST)
            if form_change_pass.is_valid():
                form_change_pass.save()
                messages.success(request,"پسورد شما با موفقیت تغییر کرد")
            if acc_detail:
                form_account_detail=acc_detail_form(instance=acc_detail)
            else:
                form_account_detail=acc_detail_form()
            form_user_detail=user_detail_form(instance=request.user)
            form_notif=notifform(instance=request.user)
        elif "update_notif" in request.POST:
            form_notif=notifform(request.POST,instance=request.user)
            if form_notif.is_valid():
                form_notif.save()
                messages.success(request,"تنظیمات اطلاعیه ها بروزرسانی شد")
            form_user_detail=user_detail_form(instance=request.user)
            if acc_detail:
                form_account_detail=acc_detail_form(instance=acc_detail)
            else:
                form_account_detail=acc_detail_form()
            form_change_pass=change_password(request.user)
            
            
    else:
        acc_detail=account_detail.objects.filter(player=request.user).first()
        if acc_detail:
            form_account_detail=acc_detail_form(instance=acc_detail)
        else:
            form_account_detail=acc_detail_form()
        form_user_detail=user_detail_form(instance=request.user)
        form_change_pass=change_password(request.user)
        form_notif=notifform(instance=request.user)

    context={"form_user":form_user_detail,"form_account":form_account_detail,
    "form_change_pass":form_change_pass,"form_notif":form_notif}
    return render(request,"user/account/setting.html",context)


class passwordreset(PasswordResetView):

    template_name="user/account/password_reset_form.html"
    success_url=reverse_lazy("user:reset_password_done")
    email_template_name='user/account/password_reset_email.html'
    form_class=emailvalidatepasswordreset

class passwordresetdone(PasswordResetDoneView):
    template_name="user/account/password_reset_done.html"

class passwordresetconfrim(PasswordResetConfirmView):
    template_name="user/account/password_reset_confrim.html"
    success_url=reverse_lazy("user:reset_password_complete")


class passwordresetcomplete(PasswordResetCompleteView):
    template_name="user/account/password_reset_complete.html"
