from django import template
from article.forms import newsletterform
register=template.Library()


@register.inclusion_tag("article/partials/pagination.html")
def pagination(pages,link,page_range):
    return{
        "pages":pages,
        "link":link,
        "page_range":page_range,
    }

@register.inclusion_tag("article/partials/articles.html")
def articles(articles,request):
    return{
        "articles":articles,
        "request":request,
    }

@register.inclusion_tag("article/partials/newsletterform.html")
def newsletter(request):
    form=newsletterform()
    return{
        "form":form,
        "request":request,
    }