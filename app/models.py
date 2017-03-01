from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
#from django_markdown.models import MarkdownField

from django.template.defaultfilters import slugify

class Product(models.Model):
	category = models.ManyToManyField('Category', related_name='category')
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, blank=True)
	price_in_vnd = models.DecimalField(max_digits=8, decimal_places=2)

	manufacturer = models.CharField(max_length=100, blank=True)
	description = models.TextField()

	photo = models.ImageField(upload_to='static/img/book_photos', blank=True)
	pub_date = models.DateTimeField(default=datetime.now)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return  str(self.id) + '/' + str(self.slug)

	def get_comments(self):
		return Comment.objects.filter(product=self)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)

class Category(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, blank=True)
	parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

	pub_date = models.DateTimeField(default=datetime.now)

	def get_absolute_url(self):
		return 'category' + '/' + self.slug

	def __unicode__(self):
		if self.parent:
			return self.name + ' : ' + self.parent.name
		else:
			return self.name

	def get_products(self):
		return Product.objects.filter(category=self)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

class Comment(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	product = models.ForeignKey('Product', related_name='product')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', null=True)

	def get_absolute_url(self):
		return self.product.get_absolute_url + '/comments/' + str(self.id)

	def __unicode__(self):
		return self.title





