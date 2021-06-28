from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
# Create your views here.
from django.db.models import Q 
from .models import SubCategory, Category, Product
from urllib.parse import unquote
from django.shortcuts import redirect

class IndexView(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_products"] = Product.objects.filter(new= True)
        context["top_selling"] = Product.objects.filter(top= True)
        context["random_3_1"] = Product.objects.all().order_by('?')[:3]
        context["random_3_2"] = Product.objects.all().order_by('?')[:3]
        context["random_3_3"] = Product.objects.all().order_by('?')[:3]
        context["random_3_4"] = Product.objects.all().order_by('?')[:3]
        context["random_3_5"] = Product.objects.all().order_by('?')[:3]
        context["random_3_6"] = Product.objects.all().order_by('?')[:3]
        return context
    

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "productDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Product.objects.all().order_by('?')[:4] 
        return context
    



# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     sub_cat = SubCategory.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         try:
#             category = get_object_or_404(Category, slug=category_slug)
#             products = products.filter(sous_category__tree__category=category)
#         except:
#             category = get_object_or_404(SubCategory, slug=category_slug)
#             products = products.filter(sous_category=category)

#     return render(request,
#                   'catalogue.html',
#                   {'category': category,
#                    'categories': categories,
#                    'sous_categories': sub_cat,
#                    'products': products})


def new_product_list(request):
    category = None
    categories = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    products = Product.objects.filter(available=True,new=True)
    return render(request,
                  'catalogue.html',{
                  'categories': categories,
                   'sous_categories': sub_cat,
                  'products': products})


class CategoryProductsView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 15
    template_name = "catalogue.html"

    def get_queryset(self, *args, **kwargs): # new
        
        products = Product.objects.filter(available=True)
        try:
            category = get_object_or_404(Category, slug=self.kwargs['slug'])
            products = products.filter(sous_category__tree__category=category)
        except:
            category = get_object_or_404(SubCategory, slug=self.kwargs['slug'])
            products = products.filter(sous_category=category)
        return products
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["sous_categories"] = SubCategory.objects.all()
        # context["products"] = Product.objects.all()
        return context


class ProductsView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 15
    template_name = "catalogue.html"

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        new = self.request.GET.get('new')
        top = self.request.GET.get('top')
        if max and new and top:
            products = Product.objects.filter(price__range=[min, max], available=True, new= True, top=True)
        elif max and new:
            products = Product.objects.filter(price__range=[min, max], available=True,new= True)
        elif max and top:
            products = Product.objects.filter(price__range=[min, max], available=True, top=True)
        elif top and new:
            products = Product.objects.filter(available=True,new= True, top=True)
        elif max:
            products = Product.objects.filter(price__range=[min, max], available=True)
        elif new:
            products = Product.objects.filter(available=True,new= True)
        elif top:
            products = Product.objects.filter( available=True, top=True)
        elif query:
            if len(query) > 2:
                by_2 = [query[i:i+2] for i in range(0, len(query), 2)][0]
                by_1 = [query[i:i+2] for i in range(0, len(query), 2)][1:]
                print('the sring split one  ', by_2)
                print('the sring towo', by_1)
                for i in by_1:
                    products = Product.objects.filter(
                            Q(name__icontains=by_2) & Q(name__icontains=i)
                            )
                    if not len(products):
                        products = Product.objects.filter(
                            Q(name__icontains=by_2) | Q(name__icontains=i)
                            )
                # products = Product.objects.filter(name__regex=r'(?i)dragx[\s\w]+')
                # products = Product.objects.filter(name__icontains=by_2, name__icontains=by_1)# erreur
                # products = Product.objects.filter(name__icontains=query)
                    print('JE SUISS LAAAAAA EXCEPTIO N TXwO', products)
            else: 
                products = Product.objects.filter(name__icontains=query)
        else :
            products = Product.objects.all()
        return products
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["sous_categories"] = SubCategory.objects.all()
        # context["products"] = Product.objects.all()
        return context

def redirect_to_shop_view(request):
    response = redirect('main:Products')
    return response