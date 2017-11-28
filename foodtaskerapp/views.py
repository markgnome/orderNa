from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from foodtaskerapp.forms import UserForm, RestaurantForm

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

@login_required(login_url='/restaurant/sign-in/')
def restaurant_home(request):
    return render(request, 'restaurant/index.html', {})

def restaurant_sign_up (request):
    user_form = UserForm()
    restaurant_form = RestaurantForm()
    return render(request, 'restaurant/sign_up.html', {
        "user_form": user_form,
        "restaurant_form": restaurant_form
    })
