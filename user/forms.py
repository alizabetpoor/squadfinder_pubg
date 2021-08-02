from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from .models import User,account_detail
from django.forms import ModelForm, fields, models, widgets
from crispy_forms.helper import FormHelper
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm



class signupfrom(UserCreationForm):

    def __init__(self, *args,**kwargs):

        super(signupfrom,self).__init__(*args,**kwargs)

        self.fields["username"].help_text=None
        self.fields["first_name"].help_text="اختیاری"
        self.fields["last_name"].help_text="اختیاری"
        self.fields["password1"].label="پسورد"
        self.fields["password1"].help_text=None
        self.fields["password2"].label="تایید پسورد"
        self.fields["password2"].help_text=None
    class Meta:
        model=User
        fields=("username","email","first_name","last_name","password1","password2")

    UserCreationForm.error_messages["username_exist"]=_("این نام کاربری در سایت موجود است.",)
    UserCreationForm.error_messages["email_exist"]=_("این ایمیل در سایت موجود است.",)
    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user=User.objects.filter(username=username).first()
        if user:
            raise ValidationError(
                self.error_messages['username_exist'],
                code='username_exist',
            )
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        user=User.objects.filter(email=email).first()
        if user:
            raise ValidationError(
                self.error_messages['email_exist'],
                code='email_exist',
            )
        return email

class loginform(AuthenticationForm):
    AuthenticationForm.error_messages['invalid_login']=_("یوزرنیم یا پسورد اشتباه است، دوباره امتحان کنید.",)


class acc_detail_form(ModelForm):
    def __init__(self, *args,**kwargs):

        super(acc_detail_form,self).__init__(*args,**kwargs)
        self.fields["role"].label="نقش"
        self.fields["start_season"].label="فصل شروع بازی"
            
    class Meta:
        model=account_detail
        fields=["rank","start_season","role","server","level"
                ,"id_game","username_game","kd","time_to_play",]



class user_detail_form(ModelForm):
    def __init__(self, *args,**kwargs):

        super(user_detail_form,self).__init__(*args,**kwargs)
        self.fields["username"].disabled=True
        self.fields["username"].help_text=None
        self.fields["email"].disabled=True
        self.fields["phone_verify"].disabled=True
        self.fields["email_verify"].disabled=True
        self.fields['username'].label = False
        self.fields["email"].label = False
        # self.helper=FormHelper()
        # self.helper.form_show_labels = True
        # for field in user_detail_form.Meta.unlabelled_fields:
        #     self.fields[field].label = False
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","phonenumber"
                ,"phone_verify","email_verify",]


class change_password(PasswordChangeForm):
    pass

class notifform(ModelForm):


    class Meta:
        model=User
        fields=["email_notif","phone_sms"]




class emailvalidatepasswordreset(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).first():
            msg = _("ایمیل شما در سایت موجود نمیباشد")
            self.add_error('email', msg)
        return email