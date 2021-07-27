from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Squad_Article
# Create your views here.

def home(request,page=1):
    articles=Squad_Article.objects.all().order_by("-publish")
    paginate=Paginator(articles,3)
    article_page=paginate.get_page(page)
    page_range=paginate.get_elided_page_range(page, on_each_side=1, on_ends=2)
    page_range=list(page_range)

    context={"articles":article_page,"page_range":page_range}
    return render(request,"article/home.html",context=context)