from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView
from ..models import Contract
from ..forms import ContractForm


class RequiredLogin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')


class ContractList(RequiredLogin, ListView):
    model = Contract
    permission_required = ["crm_app.view_contract"]
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"


class ContractDetail(RequiredLogin, DetailView):
    model = Contract
    permission_required = ["crm_app.view_contract"]
    template_name = "contracts/contracts-detail.html"
    pk_url_kwarg = "contract_id"


class ContractCreate(RequiredLogin, CreateView):
    model = Contract
    permission_required = ["crm_app.add_contract"]
    template_name = "contracts/contracts-create.html"
    form_class = ContractForm
    success_url = reverse_lazy('contracts')


class ContractDelete(RequiredLogin, DeleteView):
    model = Contract
    permission_required = ["crm_app.delete_contract"]
    template_name = "contracts/contracts-delete.html"
    pk_url_kwarg = "contract_id"
    success_url = reverse_lazy('contracts')


class ContractUpdate(RequiredLogin, UpdateView):
    model = Contract
    permission_required = ["crm_app.change_contract"]
    template_name = "contracts/contracts-edit.html"
    form_class = ContractForm
    pk_url_kwarg = "contract_id"
    success_url = reverse_lazy('contracts')
