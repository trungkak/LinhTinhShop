"""LinhTinhShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', views.home, name='home'),
    url(r'^products/category/(?P<param>[\s\S]+)/$', views.list_products_categories ,name='list_products_categories'),
    url(r'^products/(?P<param>[\s\S]+)/$', views.product_details, name='product_details'),
    url(r'^accounts/register/$', views.SignUpView.as_view(), name='register'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.logout_view, name='logout'),
    url(r'^testview/$', views.test_view, name='testview'),
    #url(r'^markdown/', django_markdown.urls),
]
