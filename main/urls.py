from django.urls import path
from .views import IndexView, ProductDetailView, ProductsView, new_product_list, redirect_to_shop_view, CategoryProductsView
app_name ='main'
urlpatterns = [
   path('', IndexView.as_view(), name='IndexView'),
   path('produits', ProductsView.as_view(), name='Products'),
   path('produits/', redirect_to_shop_view, name='redirect_to_shop_view'),
   # path('produits/<slug:category_slug>/', product_list, name='prod-by-cat'),
   path('produits/<slug:slug>/', CategoryProductsView.as_view(), name='prod-by-cat'),
   # path('produits/<slug:category_slug>/', product_list, name='prod-by-sub-cat'),
   path('produits/<slug:slug>/', CategoryProductsView.as_view(), name='prod-by-sub-cat'),
   path('produits/new', new_product_list, name='prod-new'),
   # path('produits/<slug:category_slug>/', product_list, name='prod-by-sub-cat'),
   path('produits/produit/<slug:slug>/', ProductDetailView.as_view(), name='productDetail'),
   
   #  path('vapecity/', views.vapecity, name='vapecity'),
   #  path('contact/', views.ContactView.as_view(), name='ContactView'),
]