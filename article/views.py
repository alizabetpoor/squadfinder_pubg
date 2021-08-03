from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse,reverse_lazy
from django.core.paginator import Paginator
from .models import Squad_Article,Newsletter
import operator
from user.models import User,account_detail
from django.contrib.auth.decorators import login_required
from functools import reduce
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import (
    AUTHORACCESSMIXIN,
    FORMVALIDATEMIXIN,
    ARTICLEFIELDSMIXIN,
    ACCOUNTDETAILMIXIN,
    )
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import newsletterform, searchbar
from django.views.decorators.http import require_POST
# Create your views here.


_article_per_page=5


def home(request,page=1):
    articles=Squad_Article.objects.all().order_by("-publish")
    paginate=Paginator(articles,_article_per_page)
    article_page=paginate.get_page(page)
    page_range=paginate.get_elided_page_range(page, on_each_side=1, on_ends=2)
    page_range=list(page_range)
    context={"articles":article_page,"page_range":page_range}
    return render(request,"article/home.html",context=context)


def article(request,article_id):
    article=get_object_or_404(Squad_Article,pk=article_id)

    context={"article":article}
    return render(request,"article/article.html",context)


class Create_Article(LoginRequiredMixin,ACCOUNTDETAILMIXIN,ARTICLEFIELDSMIXIN,FORMVALIDATEMIXIN,CreateView):
    model=Squad_Article
    template_name="article/article_create_update.html"
    success_url=reverse_lazy("article:home")



class Update_Article(LoginRequiredMixin,AUTHORACCESSMIXIN,ARTICLEFIELDSMIXIN,FORMVALIDATEMIXIN,UpdateView):
    model=Squad_Article
    template_name="article/article_create_update.html"
    def get_success_url(self):
          article_id=self.kwargs['pk']
          return reverse_lazy('article:article', kwargs={'article_id': article_id})


class Delete_Article(LoginRequiredMixin,AUTHORACCESSMIXIN,DeleteView):
    model=Squad_Article
    success_url=reverse_lazy("article:home")
    template_name="article/article_delete.html"


def teams_article(request,page=1):
    form=searchbar(request.POST)
    if request.method=="POST":
        if form.is_valid():
            server=form.cleaned_data["server"]
            role=form.cleaned_data["role"]
            min_kd=form.cleaned_data["min_kd"]
            min_rank=form["min_rank"].value()
            return redirect(reverse("article:teams")+ f"?server={server}&role={role}&min_kd={min_kd}&min_rank={min_rank}")
    server=request.GET.get("server")
    role=request.GET.get("role")
    min_kd=request.GET.get("min_kd")
    min_rank=request.GET.get("min_rank")
    if server or role or min_kd or min_rank:
        role=role.replace(" ","")
        role=role.replace("'","")
        role=role[1:-1]
        role=role.split(",")
        if not min_kd.replace('.','',1).isdigit():
            min_kd=0
        if not min_rank.isdigit():
            min_rank=0
        if role==[""] or len(role)>4:
            articles=Squad_Article.objects.filter(
            Q(server__contains=server) & 
            Q(min_kd__gte=min_kd) &
            Q(min_rank__gte=min_rank)
            ).order_by("-publish")
        else:
            articles=Squad_Article.objects.filter(
                Q(server__contains=server) & 
                Q(min_kd__gte=min_kd) &
                Q(min_rank__gte=min_rank)
                ).filter(reduce(operator.and_, (Q(role__contains=x) for x in role))).order_by("-publish")

    else:

        articles=Squad_Article.objects.all().order_by("-publish")
        form=searchbar()
    paginate=Paginator(articles,_article_per_page)
    query=request.get_full_path()
    if "?" in query:
        query=query.split("?")[1]
    else:
        query=""
    article_page=paginate.get_page(page)
    page_range=paginate.get_elided_page_range(page, on_each_side=1, on_ends=2)
    page_range=list(page_range)
    context={"form":form,"articles":article_page,"page_range":page_range,"query":query}
    return render(request,"article/teams.html",context)
@login_required
def accept(request,article_id,username):
    article=get_object_or_404(Squad_Article,pk=article_id)
    user=get_object_or_404(User,username=username)
    if article.author==request.user or request.user==request.user.is_superuser:
        if user in article.apply.all():
            if user not in article.rejected.all():
                article.accepted.add(user)
                messages.success(request,f"شما یوزر {user.username} را قبول کردید")
    return redirect("article:article",article_id=article_id)
@login_required
def reject(request,article_id,username):
    article=get_object_or_404(Squad_Article,pk=article_id)
    user=get_object_or_404(User,username=username)
    if article.author==request.user or request.user==request.user.is_superuser and article.author != user:
        if user in article.apply.all():
            if user not in article.accepted.all():
                article.rejected.add(user)
                messages.warning(request,f"شما یوزر {user.username} را رد کردید")
    return redirect("article:article",article_id=article_id)

@login_required
def request(request,article_id):
    article=get_object_or_404(Squad_Article,pk=article_id)
    user=request.user
    acc_detail=account_detail.objects.filter(player=user).first()
    if acc_detail:
        if  user == user.is_superuser or article.author != user:
            if user not in article.apply.all():
                article.apply.add(user)
                messages.success(request,"شما درخواست خود را فرستادید")
    else:
        messages.error(request,"لطفا ابتدا اطلاعات اکانت خود را تکمیل کنید")
        return redirect("user:user_setting")
    return redirect("article:article",article_id=article_id)

@require_POST
def register_newsletter(request):
    form=newsletterform(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"ایمیل شما با موفقیت ثبت شد")

    else:
        error_msg=form["email"].errors.as_text()

        messages.error(request,error_msg)
    return redirect(reverse("article:home"))


@login_required
def user_articles(request,page=1):
    user=request.user
    articles=Squad_Article.objects.filter(author=user)
    paginate=Paginator(articles,_article_per_page)
    article_page=paginate.get_page(page)
    page_range=paginate.get_elided_page_range(page, on_each_side=1, on_ends=2)
    page_range=list(page_range)
    context={"articles":article_page,"page_range":page_range}
    return render(request,"article/user_article.html",context=context)
