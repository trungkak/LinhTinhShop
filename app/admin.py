from django.contrib import admin
from .models import Product, Category, Comment
#from django_markdown.admin import MarkdownModelAdmin

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)