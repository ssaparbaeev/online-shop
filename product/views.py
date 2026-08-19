from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductModel
from django.contrib.auth.forms import UserCreationForm
import random


# Create your views here.
def home_view(request):
    products = ProductModel.objects.all()
    return render(request, template_name='home.html', context={
        'products': products
    })


def add_cart_view(request, id):
    cart = request.session.get('cart', [])
    if id in cart:
        cart.remove(id)
    else:
        cart.append(id)

    request.session['cart'] = cart
    return redirect('/')


def cart_list_view(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(id__in=cart)
    return render(request, template_name='cart_list.html', context={
        'products': products
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})














