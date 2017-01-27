from django.shortcuts import render
from django.http import HttpResponse
from amaze.models import Product, Category, Company, Image

# Create your views here.

def index(request):
	return render(request, 'amaze/index.html')

def shop(request):
	product_list = Product.objects.all().order_by('name')
	context_dict = {'list':product_list}
	return render(request, 'amaze/shop.html', context_dict)

def single_product(request, product_slug):
	return render(request, 'amaze/single-product.html')