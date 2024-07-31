from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as gn

from ..models import Product
from ..forms import ProductForm


class RequiredLogin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')


class ProductList(RequiredLogin, gn.ListView):
    model = Product
    permission_required = ["crm_app.view_product"]
    template_name = "products/products-list.html"
    context_object_name = "products"


class ProductDetail(RequiredLogin, gn.DetailView):
    model = Product
    permission_required = ["crm_app.view_product"]
    template_name = "products/products-detail.html"
    pk_url_kwarg = "product_id"


class ProductDelete(RequiredLogin, gn.DeleteView):
    model = Product
    permission_required = ["crm_app.delete_product"]
    template_name = "products/products-delete.html"
    pk_url_kwarg = "product_id"
    success_url = reverse_lazy('products')


class ProductCreate(RequiredLogin, gn.CreateView):
    model = Product
    permission_required = ["crm_app.add_product"]
    template_name = "products/products-create.html"
    form_class = ProductForm
    success_url = reverse_lazy('products')


class ProductUpdate(RequiredLogin, gn.UpdateView):
    model = Product
    permission_required = ["crm_app.change_product"]
    template_name = "products/products-edit.html"
    form_class = ProductForm
    pk_url_kwarg = "product_id"
    success_url = reverse_lazy('products')
