from django import template
from amaze.models import Product

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_count(context):
	request = context['request']
	cart = request.session.get('cart', {})
	return len(cart)

@register.simple_tag(takes_context=True)
def cart_amount(context):
	request = context['request']
	cart = request.session.get('cart', {})
	keys = list(cart.keys())
	product_list= []
	sum = 0
	quantity = list(cart.values())
	for id in keys:
		product_list += Product.objects.filter(id=id)
	for product,qty in zip(product_list, quantity):
		sum += product.price * int(qty)
	return sum