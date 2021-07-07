from django.contrib import auth
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from .models import User,account_detail
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request
from .forms import signupfrom,loginform,acc_detail_form,user_detail_form
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
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

class edit_user_detail(LoginRequiredMixin,UpdateView):
    model=User
    template_name="user/account/user_detail.html"
    form_class=user_detail_form
    success_url=reverse_lazy("user:user_detail")
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

def account_profile(request,username):
    user=get_object_or_404(User,username=username)
    context={"pk_user":user}
    return render(request,"user/account/profile.html",context=context)