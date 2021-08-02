from django.contrib import admin
from .models import Squad_Article,Newsletter
# Register your models here.
class Squad_Article_Admin(admin.ModelAdmin):
    list_display=["author","role","server","min_rank","min_kd","publish",]

admin.site.register(Squad_Article,Squad_Article_Admin)
admin.site.register(Newsletter)