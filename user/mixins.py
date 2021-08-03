from django.shortcuts import redirect

class CHECKUSERMIXIN:
    def dispatch(self,request,*args,**kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request,*args,**kwargs)
        else:
            return redirect("user:user_setting")