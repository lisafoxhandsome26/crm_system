from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as gn

from ..models import Customer, Advertisement
from ..forms import CustomerForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class CustomerList(RequiredLogin, gn.ListView):
    model = Customer
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomerDetail(RequiredLogin, gn.DetailView):
    model = Customer
    template_name = "customers/customers-detail.html"
    pk_url_kwarg = "customer_id"


class CustomerDelete(RequiredLogin, gn.DeleteView):
    model = Customer
    pk_url_kwarg = "customer_id"
    template_name = "customers/customers-delete.html"
    success_url = reverse_lazy('customers')


class CustomerUpdate(RequiredLogin, gn.UpdateView):
    model = Customer
    form_class = CustomerForm
    pk_url_kwarg = "customer_id"
    template_name = "customers/customers-edit.html"
    success_url = reverse_lazy('customers')


class CustomerCreate(RequiredLogin, gn.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers-create.html"

    def form_valid(self, form):
        name = form.cleaned_data['lead']
        ads = Advertisement.objects.get(leads=name)
        ads.customers_count += 1
        ads.save()
        form.save()
        return redirect('customers')
