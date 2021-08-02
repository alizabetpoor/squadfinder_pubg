from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404,redirect
from .models import Squad_Article
from user.models import account_detail
from django.contrib import messages




class ARTICLEFIELDSMIXIN:
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_superuser:
            self.fields=["author","role","server","min_rank","min_kd","min_level","min_time_to_play","apply","accepted","rejected","publish",]
        else:
            self.fields=["role","server","min_rank","min_kd","min_level","min_time_to_play"]

        return super().dispatch(request,*args, **kwargs)


class FORMVALIDATEMIXIN:
    def form_valid(self,form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj=form.save(commit=False)
            self.obj.author=self.request.user
        return super().form_valid(form)


class AUTHORACCESSMIXIN:
    def dispatch(self,request,pk,*args,**kwargs):
        article=get_object_or_404(Squad_Article,pk=pk)
        if article.author == request.user or request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            return HttpResponseForbidden("شما اجازه دسترسی به این صفحه را ندارید")

class ACCOUNTDETAILMIXIN:
    def dispatch(self,request,*args,**kwargs):
        acc_detail=account_detail.objects.filter(player=request.user).first()
        if acc_detail:
            return super().dispatch(request,*args,**kwargs)
        else:
            messages.warning(request,"ابتدا اطلاعات اکانت خود را وارد کنید.")
            return redirect("user:user_setting")