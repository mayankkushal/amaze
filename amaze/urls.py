from django.conf.urls import url
from amaze import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^shop', views.shop, name='shop'),
	url(r'^product/(?P<product_slug>[\w\-]+)',views.single_product, name='product'),
	url(r'^cart', views.cart, name='cart'),
	url(r'^add_cart', views.add_cart, name='add_cart'),
	url(r'^view_cart', views.view_cart, name='view_cart'),
	url(r'^remove', views.remove_item, name='remove_item'),
	url(r'^empty_cart', views.empty_cart, name='empty_cart'),
	url(r'^checkout', views.checkout, name='checkout'),
	url(r'^like_check', views.like_check, name='liked'),
	url(r'^like', views.like, name='like'),
	url(r'^wishlist', views.wishlist, name='wishlist'),
]


