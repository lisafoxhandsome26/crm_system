from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as gn

from ..models import Product
from ..forms import ProductForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class ProductList(RequiredLogin, gn.ListView):
    model = Product
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetail(RequiredLogin, gn.DetailView):
    model = Product
    template_name = "products/products-detail.html"
    pk_url_kwarg = "product_id"


class ProductDelete(RequiredLogin, gn.DeleteView):
    model = Product
    pk_url_kwarg = "product_id"
    template_name = "products/products-delete.html"
    success_url = reverse_lazy('products')


class ProductCreate(RequiredLogin, gn.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/products-create.html"
    success_url = reverse_lazy('products')


class ProductUpdate(RequiredLogin, gn.UpdateView):
    model = Product
    form_class = ProductForm
    pk_url_kwarg = "product_id"
    template_name = "products/products-edit.html"
    success_url = reverse_lazy('products')
