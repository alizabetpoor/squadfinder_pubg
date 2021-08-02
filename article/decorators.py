from functools import wraps
from django.shortcuts import get_object_or_404
from .models import Squad_Article
from django.http import HttpResponseForbidden



def author_required(f):
    @wraps(f)
    def g(request,article_id,*args,**kwargs):
        article=get_object_or_404(Squad_Article,pk=article_id)
        if article.author==request.user or request.user.is_superuser:
            return f(request,article_id,*args,**kwargs)
        else:
            HttpResponseForbidden("شما به این صفحه دسترسی ندارید.")
    return g