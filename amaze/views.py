from django.shortcuts import render
from django.http import HttpResponse
from amaze.models import Product, Category, Company, Image
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
	return render(request, 'amaze/index.html')

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
	cart = request.session.get('cart', {})
	keys = list(cart.keys())
	quantity = list(cart.values())
	product_list = []
	for id in keys:
		product_list += Product.objects.filter(id=id)
	lst = zip(product_list, quantity)
	context_dict = {'lst':lst}
	return render(request, 'amaze/cart.html', context_dict)

def view_cart(request):
	cart = request.session.get('cart', {})
	return HttpResponse(cart.count())


def add_cart(request):
	cart = request.session.get('cart', {})
	pk = request.POST['pk']
	quantity = request.POST['quantity']
	cart[pk] = quantity
	request.session['cart'] = cart
	return HttpResponse()

def remove_item(request):
	cart = request.session.get('cart', {})
	pk = request.POST['pk']
	cart.pop(pk)
	request.session['cart'] = cart
	return HttpResponse()