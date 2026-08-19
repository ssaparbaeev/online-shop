from django.urls import path
from .views import home_view, add_cart_view, cart_list_view, signup

app_name = 'product'
urlpatterns = [
    path('', home_view, name='home'),
    path('add/<int:id>/', add_cart_view, name='add_cart'),
    path('cart/list', cart_list_view, name='list'),
    path('accounts/signup', signup, name='signup')
]
