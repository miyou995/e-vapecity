from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from .cart import Cart
from main.models import Product
from .models import  OrderItem, Order
from delivery.models import Wilaya
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CartAddProductForm, OrderCreateForm, OrderFormWithOutQuantity
from django.template.loader import render_to_string
# import weasyprint

class CartView(TemplateView):
    template_name = "cart.html"
    

# class CheckoutView(TemplateView):
#     template_name = "checkout.html"

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
        # print('baskets details', list(cart))
        # print('Wach ahda item details', item)
    # for item in cart:
    #     item['update_quantity_form'] = CartAddProductForm(initial={ 'quantity': item['quantity']})
    #     item['total'] = item['product'].price * item['quantity']
    #     items.append(item)
    #     products.append(item['product'])
    context = {
        'cart': cart,
        # 'coupon_apply_form': coupon_apply_form
    }
    return render(request, 'cartView.html', context)

def cart_add_one_product(request, product_id):
    cart = Cart(request)
    # Get the product that we want to add
    product = get_object_or_404(Product, id= product_id, available=True)
    
    if product:
        quantity = 1
        cart.add_one(
                product=product,
                quantity=quantity,
        )
        return redirect('order:cart_detail')
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    try:
        if form.is_valid():
                cd = form.cleaned_data
                cart.add(
                    product=product,
                    quantity=cd['quantity'],
                    override_quantity=cd['override']
                )
                print('the Cart two', cart)
                return redirect('order:cart_detail')
    except:
        return redirect('/')



@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('order:cart_detail')


def order_create_one_product(request,product_id=None):
 
    form = OrderCreateForm()
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        form = OrderCreateForm(request.POST)
        print(
                'le FORMULAIRE', form
                )
        if form.is_valid():
            cd = form.cleaned_data
            quantity=cd['quantity']
            order = form.save()
            print('le formulaire est valid', quantity)
            # print('ORDER ITEM', order.quantity)
            OrderItem.objects.create(order=order,product=product,price=product.price,quantity=quantity)
                # order_created.delay(order.id)
                # order = Order.objects.get(id=order_id)
                # subject = f'Commande N°: {order.id}'
                # message = f'Chére {order.first_name},\n\n' \
                #         f'vous avez passer une commande avec succés' \
                #         f'votre identifiant de commande est le: {order.id}'
                # mail_sent = send_mail(subject, message, 'inter.taki@gmail.com',[order.email])
            return render(request, 'created.html', {'order': order})
            # print('ORDER ITEM')
            # return render(request, 'created.html', {'order': order})
        else:
            # print('yhnooo')
            return redirect(reverse('main:IndexView'))
    return render(request, 'productDetail.html', { 'form' : form})




def order_create(request):
    cart = Cart(request)
    wilayas= Wilaya.objects.all().order_by('name') 
    form = OrderFormWithOutQuantity()
    print('INIT FORM', OrderFormWithOutQuantity())
    if cart.__len__() :
        print('request', request.method)
        if request.method == 'POST':
            form = OrderFormWithOutQuantity(request.POST)
            if form.is_valid():
                print('le formulaire est valid')
                order = form.save()
                # try:
                print('carte ========>',cart)
                for item in cart:
                    OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
                cart.clear()
                return render(request, 'created.html', {'order': order})
    else: 
        return redirect(reverse('main:IndexView'))
    return render(request, 'order_create.html', {'cart':cart, 'form' : form, 'wilayas': wilayas})


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('order_pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    # # ajouter le style plus t ard erreur ???
    # weasyprint.HTML(string=html).write_pdf(response)
    return response


