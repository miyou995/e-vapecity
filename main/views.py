from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView, ListView
# Create your views here.
from django.db.models import Q 
from .models import SubCategory, Category, Product

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
    

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    sub_cat = SubCategory.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        try:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(sous_category__tree__category=category)
        except:
            category = get_object_or_404(SubCategory, slug=category_slug)
            products = products.filter(sous_category=category)

    return render(request,
                  'catalogue.html',
                  {'category': category,
                   'categories': categories,
                   'sous_categories': sub_cat,
                   'products': products})


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

class ProductsView(ListView):
    context_object_name = 'products'
    model = Product
    paginate_by = 15
    template_name = "catalogue.html"

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        min = self.request.GET.get('min')
        max = self.request.GET.get('max')
        if query and min and max:
            products = Product.objects.filter(price__range=[min, max], name__icontains=query)
            # products = Product.objects.filter(name__icontains=query)
            print('JE SUISS LAAAAAA EXCEPTION ONE')
        elif query and not min:
            products = Product.objects.filter(name__icontains=query)
            print('JE SUISS LAAAAAA EXCEPTIO N TXwO')
        else :
            products = Product.objects.all()
        return products
    


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["sous_categories"] = SubCategory.objects.all()
        # context["products"] = Product.objects.all()
        return context