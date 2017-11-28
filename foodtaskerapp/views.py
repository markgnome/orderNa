from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/index.html', {})
