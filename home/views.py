# views.py
from .form import ProductForm, CategoryForm, UserRegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category, ShoppingCart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.cache import cache

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            error_message = 'Invalid username or password.'
    else:
        error_message = None
    return render(request, 'login.html', {'error_message': error_message})

def newproduct(request):
    if request.method == 'POST':
        p_form = ProductForm(request.POST, request.FILES) 
        if p_form.is_valid():
            product = p_form.save(commit=False)
            category_id = request.POST.get('category')
            product.category = get_object_or_404(Category, category_id=category_id)
            product.save()
            return redirect('display', product_id=product.product_id, category_id=product.category.category_id)
    else:
        p_form = ProductForm()
    return render(request, 'newproduct.html', {'p_form': p_form})


def newcategory(request):
    if request.method == 'POST':
        c_form = CategoryForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('newproduct')
    else:
        c_form = CategoryForm() 
    messages.success(request,'New Category has been created')
    return render(request, 'newcategory.html', {'cform': c_form})

def home(request):
  return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')

def display(request, product_id, category_id):
    categories = Category.objects.all()
    
    if cache.get('products'):
        products=cache.get('products')
        
    else:
        products = Product.objects.all()
        cache.set('products', products)
    
    return render(request, 'display.html', {'categories': categories, 'products': products})

from django.contrib import messages
 
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    cart_item, created = ShoppingCart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1, 'totalprice': product.product_price, 'totalcartprice': product.product_price}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.totalprice = cart_item.quantity * product.product_price
        cart_item.totalcartprice += product.product_price  
        cart_item.save()
    messages.success(request, f"{product.product_name} was added to your cart.")
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart_items = ShoppingCart.objects.filter(user=request.user)
    total_cart_value = sum(item.totalprice for item in cart_items)  
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_cart_value': total_cart_value})

def remove_item(request, product_id):
    if request.method == "POST":
        cart_item = get_object_or_404(ShoppingCart, product__pk=product_id, user=request.user)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.totalprice = cart_item.quantity * cart_item.product.product_price
            cart_item.save()
        else:
            cart_item.delete()
        return redirect('cart_detail')
