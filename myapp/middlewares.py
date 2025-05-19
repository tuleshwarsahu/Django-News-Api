#******AuthenticatedUserMiddleware.py********
from django.shortcuts import redirect

def auth(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper

def guest(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper