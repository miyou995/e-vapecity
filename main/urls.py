from django.urls import path
from .views import IndexView, ProductDetailView, ProductsView, product_list, new_product_list
app_name ='main'
urlpatterns = [
   path('', IndexView.as_view(), name='IndexView'),
   path('produits', ProductsView.as_view(), name='Products'),
   path('produits/<slug:category_slug>/', product_list, name='prod-by-cat'),
   path('produits/<slug:category_slug>/', product_list, name='prod-by-sub-cat'),
   path('produits/new', new_product_list, name='prod-new'),
   # path('produits/<slug:category_slug>/', product_list, name='prod-by-sub-cat'),
   path('produits/produit/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),
   
   #  path('vapecity/', views.vapecity, name='vapecity'),
   #  path('contact/', views.ContactView.as_view(), name='ContactView'),
]