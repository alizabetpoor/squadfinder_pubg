from django.db import models
from multiselectfield import MultiSelectField
from user.models import User,ROLE_CHOICES,SERVER_CHOICES
from django.utils import timezone
# Create your models here.
class Squad_Article(models.Model):
    class Meta:
        verbose_name="پست اسکواد"
        verbose_name_plural="پست اسکواد ها"
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,verbose_name="نویسنده",related_name="article")
    role=MultiSelectField(max_length=8,max_choices=4,choices=ROLE_CHOICES,verbose_name="نقش")
    server=models.CharField(max_length=2,choices=SERVER_CHOICES,verbose_name="سرور")
    min_rank=models.CharField(max_length=30,verbose_name="حداقل رنک")
    min_kd=models.FloatField(max_length=5,verbose_name="حداقل kd")
    min_level=models.FloatField(max_length=5,verbose_name="حداقل level")
    apply=models.ManyToManyField(User,blank=True,related_name="requested",verbose_name="متقاضیان")
    accepted=models.ManyToManyField(User,blank=True,related_name="accepted",verbose_name="متقاضیان قبول شده")
    rejected=models.ManyToManyField(User,blank=True,related_name="rejected",verbose_name="متقاضیان رد شده")
    publish=models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def count_apply(self):
        self.apply.objects.count()
    def count_accepted(self):
        self.apply.objects.count()
    def count_rejected(self):
        self.apply.objects.count()