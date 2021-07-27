from django import template

register=template.Library()


@register.inclusion_tag("article/partials/pagination.html")
def pagination(pages,link,page_range):
    return{
        "pages":pages,
        "link":link,
        "page_range":page_range,
    }
