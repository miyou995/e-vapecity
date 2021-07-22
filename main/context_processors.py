from django.shortcuts import render , get_object_or_404
from .models import Category
from order.cart import Cart

def cart(resquest):
    return {'cart':Cart(resquest)}

def category(request):
    categories = Category.objects.all()
    return {
            'categories' : categories
        }
    
# def majeur(request):
#     major = request.session["major"]
#     return {
#             'major' : major
#         }
    