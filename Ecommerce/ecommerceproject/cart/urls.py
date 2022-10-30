
from django.urls import path,include
from .import views

app_name='cart'


urlpatterns = [
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cartdet',views.cart_detail,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('fullremove/<int:product_id>/',views.full_remove,name='full_remove'),
    path('place',views.payment,name='payment'),
    path('ordersuccessful',views.ordersuccess,name='ordersuccess')

]