from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category,Product,Order,OrderItem
from .forms import OrderForm
from . cart import Cart

# Create your views here.

def index (request):
    pro = Product.objects.all()
    return render (request,'index.html',{'pro':pro})

def checkout (request):
   
    if request.method == 'POST':
        form = OrderForm(request.POST)
        cart = Cart(request)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    # quantity=item['quantity']
                )
            cart.clear()
            return redirect('success')

    form = OrderForm()
   
    context = {
        'form':form,
        'cart':cart,
    }
    return render (request,'Checkout.html',context)

def cart (request):
    car= Cart(request)
    return render (request,'cart.html',{'cart':car})

def order (request):
    orders = Order.objects.all()
    return render (request,'order.html',{'order':orders})

def ordersingle (request,pk):
    orders = Order.objects.get(pk=pk)
    single = OrderItem.objects.filter(order=orders)
    return render (request,'ordersingle.html',{'single':single})

def productsingle (request,pk):
    prosin = Product.objects.get(pk=pk)
    return render (request,'productsingle.html',{'prosin':prosin})

def success (request):
    return render (request,'success.html')

def product (request):
    pro = Product.objects.all()
    return render (request,'products.html',{'pro':pro})

def cart_add (request, pk):
    cart=Cart(request)
    cart.add(pk)
    return redirect('cart')

def cart_remove (request, pk):
    cart=Cart(request)
    cart.remove(pk)
    return redirect('cart')


