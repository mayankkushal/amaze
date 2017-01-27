from django.conf.urls import url
from amaze import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^shop', views.shop, name='shop'),
	url(r'^product/(?P<product_slug>[\w\-]+)',views.single_product, name='single_product')
]


