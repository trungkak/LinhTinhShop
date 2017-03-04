from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Comment
# Create your views here.

from .forms import RegistrationForm, LoginForm, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic

from django.urls import reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse_lazy
import json
from braces import views


def test_view(request):
	template = 'layouts/test.html'

	return render(request, template, {})

def home(request):
	num = len(request.session.get('cart', {}))

	template='layouts/home.html'

	return render(request, template, {})

def list_products_categories(request, param):

	template = 'product/list_products_categories.html'

	categories = Category.objects.all()
	category_this = None

	if param == 'all':
		products = Product.objects.all()
	else:
		category_this = Category.objects.get(slug=param)

		products = category_this.get_products()

	context = {
		'categories' : categories,
		'category_this': category_this,
		'products' : products
	}

	return render(request, template, context)

def product_details(request, param):
	template = 'product/product_details.html'

	id = param.split('/')[0]

	product = Product.objects.get(pk=id)

	comments = product.get_comments()

	form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.product = product
		comment.save()
	else:
		form = CommentForm()

	context = {'product' : product, 'comments' : comments, 'form' : form}
	return render(request, template, context)

def add_to_cart(request):
	
	if request.is_ajax():
		cart = request.session.get('cart', [])
		product_id = request.GET['product_id']
		cart.append(product_id)
		request.session['cart'] = cart

		data = json.dumps(len(request.session['cart']))
		return HttpResponse(data, content_type='application/json')
	else:
		raise Http404

	return HttpResponseRedirect(request.path)

def clear_cart(request):

	if request.method == 'GET':
		request.session['cart'] = []
			
	return HttpResponseRedirect(request.path)


class SignUpView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.CreateView
):
	form_class = RegistrationForm
	form_valid_message = 'Thanks for signing up, go ahead and log in'
	model = User
	template_name = 'accounts/signup.html'

	success_url = reverse_lazy('home')

class LoginView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.FormView
):
	form_class = LoginForm
	form_valid_message = 'You\'re logged in now'
	success_url = reverse_lazy('home')
	template_name = 'accounts/login.html'

	# def get_success_url(self):
	# 	return reverse_lazy(self.request.path)

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_valid(form)


@login_required
def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('home'))