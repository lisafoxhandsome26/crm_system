from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as gn

from ..models import Lead, Advertisement
from ..forms import LeadForm


class RequiredLogin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')


class LeadList(RequiredLogin, gn.ListView):
    model = Lead
    permission_required = ["crm_app.view_lead"]
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadDetail(RequiredLogin, gn.DetailView):
    model = Lead
    permission_required = ["crm_app.view_lead"]
    template_name = "leads/leads-detail.html"
    pk_url_kwarg = "lead_id"


class LeadDelete(RequiredLogin, gn.DeleteView):
    model = Lead
    permission_required = ["crm_app.delete_lead"]
    template_name = "leads/leads-delete.html"
    pk_url_kwarg = "lead_id"
    success_url = reverse_lazy('leads')


class LeadUpdate(RequiredLogin, gn.UpdateView):
    model = Lead
    permission_required = ["crm_app.change_lead"]
    template_name = "leads/leads-edit.html"
    form_class = LeadForm
    pk_url_kwarg = "lead_id"
    success_url = reverse_lazy('leads')


class LeadCreate(RequiredLogin, gn.CreateView):
    model = Lead
    permission_required = ["crm_app.add_lead"]
    template_name = "leads/leads-create.html"
    form_class = LeadForm

    def form_valid(self, form):
        ads = form.cleaned_data['ads']
        object = Advertisement.objects.get(name=ads)
        object.leads_count += 1
        object.save()
        form.save()
        return redirect('leads')
