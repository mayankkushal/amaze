from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from amaze.models import Product, Category, Company, Image, Cart, Like
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import json


# Create your views here.

def index(request):
	product_list = Product.objects.all().order_by('-price')[:5]
	context_dict = {'product_list':product_list}
	return render(request, 'amaze/index.html', context_dict)

def shop(request):
	product_list = Product.objects.all().order_by('name')
	context_dict = {'list':product_list}
	return render(request, 'amaze/shop.html', context_dict)

def single_product(request, product_slug):
	try:
		product = Product.objects.get(slug=product_slug)
	except:
		product = None
	context_dict = {'product': product}
	return render(request, 'amaze/single-product.html', context_dict)

def cart(request):
	product_list = []
	lst = []
	cart = {}
	if request.user.is_authenticated():
		product_list = Cart.objects.filter(user=request.user)
	else:
		cart = request.session.get('cart', {})
		keys = list(cart.keys())
		quantity = list(cart.values())
		for id in keys:
			product_list += Product.objects.filter(id=id)
		lst = zip(product_list, quantity)
	context_dict = {'lst':lst, 'cart':cart, 'product_list':product_list}
	return render(request, 'amaze/cart.html', context_dict)

def checkout(request):
	return render(request, 'amaze/checkout.html')

def view_cart(request):
	cart = request.session.get('cart', {})
	return HttpResponse(cart.count())


def add_cart(request):
	pk = request.POST['pk']
	quantity = request.POST['quantity']
	if request.user.is_authenticated():
		product = Product.objects.get(id=pk)
		if product:
			try:
				entry = Cart.objects.get(user=request.user, product=product)
			except Cart.DoesNotExist:
				entry = None 
			if entry:
				if entry.quantity != quantity:
					entry.quantity = quantity
					entry.save()
			else:
				Cart.objects.create(user=request.user, product=product, quantity=quantity)
	else:
		cart = request.session.get('cart', {})
		cart[pk] = quantity
		request.session['cart'] = cart
	return HttpResponse()

def remove_item(request):
	pk = request.POST['pk']
	if request.user.is_authenticated():
		product = Product.objects.get(id=pk)
		cart = Cart.objects.get(user=request.user, product=product)
		cart.delete()
	else:
		cart = request.session.get('cart', {})
		cart.pop(pk)
		request.session['cart'] = cart
	return HttpResponse()

def empty_cart(request):
	if request.user.is_authenticated():
		Cart.objects.filter(user=request.user).delete()
	else:
		request.session['cart'] = {}
	return cart(request)

@login_required
def like(request):
	if request.method == "GET":
		id = request.GET['id']
		product = Product.objects.get(id=id)
		if product:
			new_like, created = Like.objects.get_or_create(user=request.user, product_id=id)
			if not created:
				new_like.delete()
				like = False
			else:
				like = True
			data = {'like':like}
			return HttpResponse(json.dumps(data), content_type='application/json')

def like_check(request):
	if request.method == "GET":
		id = request.GET['id']
		product = get_object_or_404(Product, id=id)
		if product:
			liked_this = Like.objects.filter(user=request.user, product=product)
			if liked_this:
				lkd = True
			else:
				lkd = False
		d = {'lkd': lkd}
		return HttpResponse(json.dumps(d), content_type='application/json')

def wishlist(request):
	like_list = Like.objects.filter(user=request.user)
	return render(request, 'amaze/wishlist.html', {'like_list':like_list})
