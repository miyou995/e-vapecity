from django.urls import path
from .views import CartView, cart_detail, cart_add_one_product, cart_add, cart_remove, order_create, admin_order_detail ,admin_order_pdf, order_create_one_product

app_name = 'order'

urlpatterns = [
   # path('', CartView.as_view(), name='CartView'),
   path('cart', cart_detail, name='cart_detail'),
   # path('checkout', CheckoutView.as_view(), name='CheckoutView'),
   path('add/<int:product_id>/', cart_add, name='cart_add'),
   path('commander', order_create, name='order_create'),
   path('ajouter-au-panier<int:product_id>/', cart_add_one_product, name='cart_add_one_product'),
   path('acheter/<int:product_id>/', order_create_one_product, name='order_create_one_product'),
   path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
   path('admin/order/<int:order_id>/', admin_order_detail, name='admin_order_detail'),
   path('admin/order/<int:order_id>/pdf/', admin_order_pdf, name='admin_order_pdf'),

]

