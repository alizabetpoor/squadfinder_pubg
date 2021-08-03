from functools import wraps
from django.shortcuts import redirect

def checkuser(func):
    @wraps(func)
    def g(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return func(request,*args,**kwargs)
        else:
            return redirect("user:user_setting")
    return g