from django.contrib import admin
from .models import User,account_detail,Rank
from django.contrib.auth.admin import UserAdmin
# Register your models here.

UserAdmin.fieldsets[1][1]['fields']+=("phonenumber",
                                    "phone_verify",
                                    "email_verify",
)

UserAdmin.add_fieldsets[0][1]["fields"]=("email",'username',
                                        'password1', 'password2')

UserAdmin.list_display = ('username', 'email',"phonenumber", 'first_name',
                         'last_name','is_staff',"email_verify","phone_verify")

admin.site.register(User,UserAdmin)

class Account_Detail_Admin(admin.ModelAdmin):
    list_display=["get_player_username","rank","start_season","get_role_display","server",]

class Rank_Admin(admin.ModelAdmin):
    list_display=["title","position"]

admin.site.register(Rank,Rank_Admin)
admin.site.register(account_detail,Account_Detail_Admin)
