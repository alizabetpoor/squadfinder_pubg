from django.db import models
from multiselectfield import MultiSelectField
from user.models import User,ROLE_CHOICES,SERVER_CHOICES,Rank
from django.utils import timezone
from user.models import validate_min
# Create your models here.
class Squad_Article(models.Model):
    class Meta:
        verbose_name="پست اسکواد"
        verbose_name_plural="پست اسکواد ها"
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name="نویسنده",related_name="article")
    role=MultiSelectField(max_length=11,max_choices=4,choices=ROLE_CHOICES,verbose_name="نقش")
    server=models.CharField(max_length=2,choices=SERVER_CHOICES,verbose_name="سرور")
    min_rank=models.ForeignKey(Rank,on_delete=models.CASCADE,related_name="squad_article",verbose_name="حداقل رنک")
    min_kd=models.FloatField(max_length=5,validators=[validate_min],verbose_name="حداقل kd")
    min_level=models.IntegerField(verbose_name="حداقل level",validators=[validate_min],)
    min_time_to_play=models.IntegerField(verbose_name="حداقل تایم بازی در روز(ساعت)",validators=[validate_min],)
    apply=models.ManyToManyField(User,blank=True,related_name="requested",verbose_name="متقاضیان")
    accepted=models.ManyToManyField(User,blank=True,related_name="accepted",verbose_name="متقاضیان قبول شده")
    rejected=models.ManyToManyField(User,blank=True,related_name="rejected",verbose_name="متقاضیان رد شده")
    publish=models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def new_apply(self):
        count_new_apply=self.apply.count() - (self.accepted.count() + self.rejected.count())
        if count_new_apply<0:
            count_new_apply=0
        return count_new_apply


class Newsletter(models.Model):
    class Meta:
        verbose_name="خبرنامه"
        verbose_name_plural="خبرنامه ها"
    email=models.EmailField(unique=True,null=False,verbose_name="ایمیل")
    join=models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.email