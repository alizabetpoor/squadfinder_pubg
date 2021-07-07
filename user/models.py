from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.





def validate_min(value):
    if value < 1:
        raise ValidationError(
            _(f'عدد باید بزرگ تر از 0 باشد'),
        )

ROLE_CHOICES = [
    ('sn', 'sniper'),
    ('ca', 'camper'),
    ('ru', 'rusher'),
    ('co', 'cover'),
    ]

SERVER_CHOICES = [
        ("EU","europe"),
        ("AS","asia"),
        ("KO","korea"),
        ("AF","africa"),
        ("US","america"),
]

class User(AbstractUser):
    email=models.EmailField(unique=True,null=False,verbose_name="ایمیل")
    phonenumber=models.CharField(max_length=13,unique=True,null=True,blank=True,default=None,verbose_name="شماره موبایل")
    phone_verify=models.BooleanField(default=False,verbose_name="وریفای ایمیل")
    email_verify=models.BooleanField(default=False,verbose_name="وریفای شماره")

    REQUIRED_FIELDS = ['email']
    def __str__(self) -> str:
        return f"{self.username}"



class account_detail(models.Model):

    class Meta:
        verbose_name="اطلاعات اکانت"
        verbose_name_plural="اطلاعات اکانت ها"
    player=models.OneToOneField(User,related_name="acc_detail",null=True,default=None,on_delete=models.CASCADE)


    rank=models.CharField(max_length=30,verbose_name="رنک بازی")
    start_season=models.IntegerField(validators=[validate_min],verbose_name="سیزن شروع بازی")
    role=MultiSelectField(max_length=8,max_choices=4,choices=ROLE_CHOICES,verbose_name="نقش")
    server=models.CharField(max_length=2,choices=SERVER_CHOICES,verbose_name="سرور")
    level=models.IntegerField(default=None,validators=[validate_min],verbose_name="لول شما")
    id_game=models.CharField(max_length=20,default=None,verbose_name="ایدی شما در بازی")
    username_game=models.CharField(default=None,max_length=60,verbose_name="یوزرنیم شما در بازی")
    kd=models.FloatField(max_length=5,default=None,verbose_name="kd شما")
    time_to_play=models.IntegerField(verbose_name="میزان ساعت بازی در روز",validators=[validate_min])
    def __str__(self) -> str:
        return f"{self.start_season}"

    def get_player_username(self):
        if self.player:
            return self.player.username
        else:
            return "-"
    get_player_username.short_description="player"

