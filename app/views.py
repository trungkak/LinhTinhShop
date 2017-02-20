from django.shortcuts import render
from .models import Product, Category
# Create your views here.


def list_products(request):
	template = 'product/list_products.html'

	products = Product.objects.all()
	categories = Category.objects.all()

	context = {'products' : products,
				'categories' : categories
			}

	return render(request, template, context)


def list_products_categories(request, param):

	template = 'product/list_products_categories.html'

	categories = Category.objects.all()

	category_this = Category.objects.get(slug=param)

	context = {
		'categories' : categories,
		'category_this': category_this
	}

	return render(request, template, context)

def product_details(request, param):
	template = 'product/product_details.html'

	id = param.split('/')[0]

	product = Product.objects.get(pk=id)
	context = {'product' : product}
	return render(request, template, context)