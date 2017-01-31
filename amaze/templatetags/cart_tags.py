from django import template
from amaze.models import Product, Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def cart_count(context):
	request = context['request']
	if request.user.is_authenticated():
		count = Cart.objects.filter(user=request.user).count()
	else:
		cart = request.session.get('cart', {})
		count = len(cart)
	return count

@register.simple_tag(takes_context=True)
def cart_amount(context):
	request = context['request']
	amount = 0
	if request.user.is_authenticated():
		cart = Cart.objects.filter(user=request.user)
		for product in cart:
			amount += product.product.price * product.quantity
	else:
		cart = request.session.get('cart', {})
		keys = list(cart.keys())
		product_list= []
		quantity = list(cart.values())
		for id in keys:
			product_list += Product.objects.filter(id=id)
		for product,qty in zip(product_list, quantity):
			amount += product.price * int(qty)
	return amount