from django.shortcuts import render
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


# Create your views here.

def log_out(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('home'))

def profile(request):
    return render(request, 'profile.html')