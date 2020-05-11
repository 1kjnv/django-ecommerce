from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.forms import PasswordChangeForm 
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.urls import reverse

import stripe
stripe.api_key = "sk_test_BJ797kl6s4vD9Lb9IAPkXWsH00hiGidJnD"

from .models import *
from .forms import *
from cart.models import *

def Base(request):
	user = request.user
	product = Item.objects.all()
	if user.is_authenticated:
		cart = Cart.objects.get(user=request.user)
		cartitem = CartItem.objects.filter(cart=cart)
		quantity = 0
		for item in cartitem:	
			quantity += item.quantity

		return render(request, 'base.html', {'products':product, 'quantity':quantity})
	else:
		return render(request, 'base.html', {'products':product})

def Home(request):
	user = request.user
	product = Item.objects.all()
	if user.is_authenticated:
		cart = Cart.objects.get(user=request.user)
		cartitem = CartItem.objects.filter(cart=cart)
		quantity = 0
		for item in cartitem:	
			quantity += item.quantity

		return render(request, 'home.html', {'products':product, 'quantity':quantity})
	else:
		return render(request, 'home.html', {'products':product})

@login_required(login_url="login")
def ProfileCart(request):
	cart = Cart.objects.get(user=request.user)
	cartitem = CartItem.objects.filter(cart=cart)
	total = 0
	quantity = 0
	for item in cartitem:
		item.subtotal  = item.quantity * item.price
		item.save()
		quantity += item.quantity
		total += item.subtotal

	return render(request, 'profile/profile_cart.html', {'cartitem':cartitem, 'total':total, 'quantity': quantity})


@login_required(login_url="login")
def InsertProduct(request):
	
	if request.method == 'POST':
		if request.POST['name'] and request.POST['price'] and request.POST['description'] and request.POST['color'] and request.POST['category'] and request.FILES['image'] and request.POST['quantity']:
			product = Item()
			product.name = request.POST['name']	
			product.price = request.POST['price']
			product.description = request.POST['description']
			product.color = request.POST['color']
			product.category = request.POST['category']
			product.image = request.FILES['image']
			product.quantity = request.POST['quantity']
			product.created_by = request.user
			product.save()
			return redirect('productlist')
		else:
			return render(request, 'product/product_form.html', {'error': 'All fields are required!'})
	else:
		return render(request, 'product/product_form.html')


def ProductList(request):
	if request.method == 'POST':
		# item = Item.objects.filter(name__icontains = str(request.POST['search']))
		# return render(request, 'product/product_list.html', {'allproducts':item})

		#item = Item.objects.filter(name__icontains = str(request.POST['search']))
		item = Item.objects.filter(name__icontains = str(request.POST['search']))
		return render(request, 'product/product_list.html', {'allproducts': item})

		page = request.GET.get('page', 1)

		paginator = Paginator(item, 1)
		try:
			items = paginator.page(page)
		except PageNotAnInteger:
			items = paginator.page(1)
		except EmptyPage:
			items = paginator.page(paginator.num_pages)
	else:
		item = Item.objects.all()
		page = request.GET.get('page', 1)

		paginator = Paginator(item, 9)
		try:
			items = paginator.page(page)
		except PageNotAnInteger:
			items = paginator.page(1)
		except EmptyPage:
			items = paginator.page(paginator.num_pages)

		return render(request, 'product/product_list.html', {'allproducts': items})

def SortedProductList(request, keyword):
	if keyword == 'allclothes':
		item = Item.objects.filter(category__icontains = 'menclothes') or Item.objects.filter(category__icontains = 'menclothes womenclothes')
		return render(request, 'product/product_list.html', {'allproducts': item})
	else:
		item = Item.objects.filter(category__iexact = str(keyword))
		return render(request, 'product/product_list.html', {'allproducts': item})

@login_required(login_url='login')
def UserProductList(request):
	product = Item.objects.filter(created_by=request.user)
	return render(request, 'product/product_by_user.html', {'productlist': product})


def UserSortedProductList(request, keyword):
	if keyword == 'allclothes':
		item = Item.objects.filter(category__icontains = 'menclothes') or Item.objects.filter(category__icontains = 'menclothes womenclothes')
		return render(request, 'product/product_list.html', {'allproducts':item})
	else:
		item = Item.objects.filter(category__iexact = str(keyword))
		return render(request, 'product/product_list.html', {'allproducts':item})


def Register(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				email = User.objects.get(email=request.POST['email'])
				return render(request, 'profile/profile_create.html', {'error':'username and/or email has already been taken'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
				login(request, user)
				cart = Cart()
				cart.user = request.user
				cart.save()
				return redirect('home')
		else:
			return render(request, 'profile/profile_create.html', {'error':'passwords should match'})
	else:
		return render(request, 'profile/profile_create.html')


def Login(request):
	if request.method == "POST":
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			login(request, user)
			if user.is_staff:
				return redirect('admindashboard')
			else:
				return redirect('home')
		else:
			return render(request, 'profile/profile_login.html', {'error': 'Username or password is incorrect!'})
	else:
		return render(request, 'profile/profile_login.html')

# shows userlist in admin page
def userlist(request):
	if request.method == 'POST':
		users = User.objects.all()
		return render(request, 'admin/users.html', {'userlist': user})
		
		page = request.GET.get('page', 1)

		paginator = Paginator(users, 1)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)
	else:
		user = User.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(user, 5)
		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		return render(request, 'admin/users.html', {'userlist':users})


def Admin_product_create(request):
	if request.method == 'POST':
		if request.POST['name'] and request.POST['price'] and request.POST['description'] and request.POST['color'] and request.POST['category'] and request.FILES['image'] and request.POST['quantity']:
			product = Item()
			product.name = request.POST['name']	
			product.price = request.POST['price']
			product.description = request.POST['description']
			product.color = request.POST['color']
			product.category = request.POST['category']
			product.image = request.FILES['image']
			product.quantity = request.POST['quantity']
			product.created_by = request.user
			product.save()
			return redirect('admindashboard')
		else:
			return render(request, 'admin/product_create.html', {'error': 'All fields are required!'})
	else:
		return render(request, 'admin/product_create.html')


def Logout(request):
	logout(request)
	return redirect('home')


def product_detail(request, product_id):
	detail = Item.objects.filter(id=product_id)
	return render(request, 'product/product_detail.html', {'product_detail': detail})

@login_required(login_url="login")
def add_to_cart(request, product_id):
	product1 = Item.objects.get(pk=product_id)
	inCart = CartItem.objects.filter(product=product1)
	cart = Cart.objects.get(user=request.user)
	products = CartItem.objects.filter(cart=cart)

	exs = False

	for i in products:
		for j in inCart:
			if i.product == j.product:
				i.quantity += 1
				i.save()
				exs = True
	
	if not exs:
		addcart = CartItem()
		addcart.product = product1
		addcart.cart = cart
		addcart.price = product1.price
		addcart.save()

	products = Item.objects.all()

	

	return redirect('cart')

def object_delete(request, product_id):
	product = Item.objects.get(pk=product_id)
	product.delete()
	return redirect('admindashboard')


@login_required(login_url="login")
def remove_from_cart(request, product_id):
	product = Item.objects.get(pk=product_id)
	card = Cart.objects.filter(user=request.user)

	if card.exists():
		cartitem = CartItem.objects.filter(product=product)
		if cartitem.exists():
			cartitem.delete()
		return redirect('cart')
	return redirect('home')


@login_required(login_url="login")
def ProfileCart(request):
	cart = Cart.objects.get(user=request.user)
	cartitem = CartItem.objects.filter(cart=cart)
	total = 0
	quantity = 0
	for item in cartitem:
		item.subtotal  = item.quantity * item.price
		item.save()
		quantity += item.quantity
		total += item.subtotal

	return render(request, 'profile/profile_cart.html', {'cartitem':cartitem, 'total':total, 'quantity': quantity})

@login_required(login_url="login")
def Billing(request):
	return render(request, "billing.html", {'error': 'you need to login'})

def ContactForm(request):
	if request.method == 'POST':
		if request.POST['username'] and request.POST['email'] and request.POST['subject'] and request.POST['message']:
			contact = Contact()
			contact.username = request.user
			contact.email = request.POST['email']
			contact.subject = request.POST['subject']
			contact.message = request.POST['message']

			contact.save()
			return redirect('home')
		else:
			return render(request, 'contact.html', {'error': 'All fields are required!'})
	else:
		return render(request, 'contact.html')

def user_detail(request, user_id):
	user = User.objects.filter(pk=user_id)
	return render(request, 'profile/profile.html', {'profile_detail': user})

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = EditProfileForm(instance=request.user)
		args = {'form': form}
		return render(request, 'profile/profile_update.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('home')
	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}

		return render(request, 'profile/change_password.html', args)

@login_required(login_url="login")
def AdminDashboard(request):
	if request.method == 'POST':
		item = Item.objects.filter(name__icontains = str(request.POST['search']))
		return render(request, 'admin.html', {'admindashboard': item})
		
		page = request.GET.get('page', 1)

		paginator = Paginator(item, 1)
		try:
			items = paginator.page(page)
		except PageNotAnInteger:
			items = paginator.page(1)
		except EmptyPage:
			items = paginator.page(paginator.num_pages)
	else:
		item = Item.objects.all()
		page = request.GET.get('page', 1)

		paginator = Paginator(item, 10)
		try:
			items = paginator.page(page)
		except PageNotAnInteger:
			items = paginator.page(1)
		except EmptyPage:
			items = paginator.page(paginator.num_pages)

		return render(request, 'admin.html', {'admindashboard':items})

@login_required(login_url='login')
def edit_product(request, product_id):
	product = Item.objects.get(pk=product_id)
	if request.method == 'POST':
		form = EditProduct(request.POST, instance=product)

		if form.is_valid():
			form.save()
			return redirect('admindashboard')
	else:
		form = EditProduct(instance=product)
		args = {'form': form}

		return render(request, 'product/product_update.html', args)

@login_required(login_url="login")
def charge(request):
	amount = 0
	cart = Cart.objects.get(user=request.user)
	cartitem = CartItem.objects.filter(cart=cart)

	total = 0
	quantity = 0
	for item in cartitem:
		item.subtotal  = item.quantity * item.price
		item.save()
		quantity += item.quantity
		total += item.subtotal
	print(total)
	
	if request.method == 'POST':
		print("Data: ", request.POST)
		amount = int(request.POST['amount'])
		customer = stripe.Customer.create(
			email = request.POST['email'],
			name = request.POST['name'],
			source = request.POST['stripeToken']
		)
		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description = 'Product Price',
			
		)
		for i in cartitem:
			orders = Order()
			orders.user = request.user
			orders.item = i.product
			orders.quantity = i.quantity
			orders.price = i.price
			orders.totalprice = i.subtotal
			orders.save()

		if cartitem.exists():
			cartitem.delete()
		return redirect(reverse('success', args=[amount]))
	else:
		return render(request, 'billing.html', {'amount': amount,'total':total, 'quantity': quantity })
	#return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'payment_success.html', {'amount': amount})

def admin_orders(request):
	if request.method == 'POST':
		orders = Order.objects.all()
		return render(request, 'admin/orders.html', {'orders': orders})
	
		page = request.GET.get('page', 1)

		paginator = Paginator(orders, 1)
		try:
			orders = paginator.page(page)
		except PageNotAnInteger:
			orders = paginator.page(1)
		except EmptyPage:
			orders = paginator.page(paginator.num_pages)
	else:
		order = Order.objects.all()
		page = request.GET.get('page', 1)
		paginator = Paginator(order, 5)
		try:
			orders = paginator.page(page)
		except PageNotAnInteger:
			orders = paginator.page(1)
		except EmptyPage:
			orders = paginator.page(paginator.num_pages)

		return render(request, 'admin/orders.html', {'orders':orders})