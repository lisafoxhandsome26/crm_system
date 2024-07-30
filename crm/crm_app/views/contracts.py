from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView, ListView
from ..models import Contract
from ..forms import ContractForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class ContractList(RequiredLogin, ListView):
    model = Contract
    template_name = "contracts/contracts-list.html"
    context_object_name = "contracts"


class ContractDetail(RequiredLogin, DetailView):
    model = Contract
    template_name = "contracts/contracts-detail.html"
    pk_url_kwarg = "contract_id"


class ContractCreate(RequiredLogin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts/contracts-create.html"
    success_url = reverse_lazy('contracts')

    # def post(self, request, *args, **kwargs):
    #     res = Contract.objects.prefetch_related('customer').prefetch_related('product').get(pk=self.pk)
    #     ad = res.customer.lead.ads
    #     prof = res.cost - ad.budget - res.product.cost
    #     ad.profit += prof
    #     ad.save()


class ContractDelete(RequiredLogin, DeleteView):
    model = Contract
    pk_url_kwarg = "contract_id"
    template_name = "contracts/contracts-delete.html"
    success_url = reverse_lazy('contracts')


class ContractUpdate(RequiredLogin, UpdateView):
    model = Contract
    form_class = ContractForm
    pk_url_kwarg = "contract_id"
    template_name = "contracts/contracts-edit.html"
    success_url = reverse_lazy('contracts')
