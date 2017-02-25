from __future__ import unicode_literals

from django.db import models
from datetime import datetime

from django.template.defaultfilters import slugify

class Product(models.Model):
	category = models.ManyToManyField('Category', related_name='category')
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=150, blank=True)
	price_in_vnd = models.DecimalField(max_digits=8, decimal_places=2)

	manufacturer = models.CharField(max_length=100, blank=True)
	description = models.TextField()

	photo = models.ImageField(upload_to='product_photo', blank=True)
	pub_date = models.DateTimeField(default=datetime.now)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return  str(self.id) + '/' + str(self.slug)

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




