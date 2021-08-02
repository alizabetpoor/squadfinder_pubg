from django.forms import ModelForm
from article.models import Squad_Article,Newsletter
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import gettext as _


class searchbar(ModelForm):
    def __init__(self, *args,**kwargs):

        super(searchbar,self).__init__(*args,**kwargs)
        self.fields["server"].widget.option_template_name="article/forms/select_option.html"
        self.fields["server"].widget.template_name="article/forms/select.html"
        self.fields["role"].required=False
        self.fields["server"].required=False
        self.fields["min_rank"].required=False
        self.fields["min_kd"].required=False
        self.fields["role"].widget.template_name="article/forms/checkbox_select.html"
        self.fields["role"].widget.option_template_name="article/forms/checkbox_option.html"
    class Meta:
        model=Squad_Article
        fields=["server","min_rank","min_kd","role"]


class newsletterform(ModelForm):
    def __init__(self, *args,**kwargs):

        super(newsletterform,self).__init__(*args,**kwargs)
        self.fields["email"].error_messages["unique"]=_("این ایمیل در خبرنامه موجود است",)
    
    class Meta:
        model=Newsletter
        fields=["email"]



