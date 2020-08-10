from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
# Create your views here.

class ProductList(LoginRequiredMixin, ListView):
    login_url = '/auth/'
    model = Product

product_list_view = ProductList.as_view()

class ProductDetail(LoginRequiredMixin, DetailView):
    login_url = '/auth/'
    model = Product
    redirect_field_name = 'home'
product_detail_view = ProductDetail.as_view()