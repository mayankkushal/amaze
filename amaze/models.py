from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=300)
	description = models.CharField(max_length=500)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Categories'

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)

		super(Category, self).save(*args, **kwargs)
	
class Company(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()

    def __str__(self):
    	return self.name

    class Meta:
    	verbose_name_plural = 'Companies'

    def save(self, *args, **kwargs):
    	if not self.id:
    		self.slug = slugify(self.name)
    	super(Company, self).save(*args, **kwargs)


class Product(models.Model):
	category = models.ForeignKey(Category)
	name = models.CharField(max_length=300)
	company = models.ForeignKey(Company)
	description = models.CharField(max_length=500)
	date = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
	slug = models.SlugField()

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

    
class Image(models.Model):
	product = models.ForeignKey(Product, related_name='images')
	image = models.ImageField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.name

class Cart(models.Model):
	user = models.ForeignKey(User, null=True)
	product = models.ForeignKey(Product)
	quantity = models.IntegerField(default=0)

	def __str__(self):
		return self.product.name

class Like(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
