from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as gn

from ..models import Customer, Advertisement
from ..forms import CustomerForm


class RequiredLogin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')


class CustomerList(RequiredLogin, gn.ListView):
    model = Customer
    permission_required = ["crm_app.view_customer"]
    template_name = "customers/customers-list.html"
    context_object_name = "customers"


class CustomerDetail(RequiredLogin, gn.DetailView):
    model = Customer
    permission_required = ["crm_app.view_customer"]
    template_name = "customers/customers-detail.html"
    pk_url_kwarg = "customer_id"


class CustomerDelete(RequiredLogin, gn.DeleteView):
    model = Customer
    permission_required = ["crm_app.delete_customer"]
    template_name = "customers/customers-delete.html"
    pk_url_kwarg = "customer_id"
    success_url = reverse_lazy('customers')


class CustomerUpdate(RequiredLogin, gn.UpdateView):
    model = Customer
    permission_required = ["crm_app.change_customer"]
    template_name = "customers/customers-edit.html"
    form_class = CustomerForm
    pk_url_kwarg = "customer_id"
    success_url = reverse_lazy('customers')


class CustomerCreate(RequiredLogin, gn.CreateView):
    model = Customer
    permission_required = ["crm_app.add_customer"]
    template_name = "customers/customers-create.html"
    form_class = CustomerForm

    def form_valid(self, form):
        name = form.cleaned_data['lead']
        ads = Advertisement.objects.get(leads=name)
        ads.customers_count += 1
        ads.save()
        form.save()
        return redirect('customers')
