from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views import generic as gn

from ..models import Lead, Advertisement
from ..forms import LeadForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class LeadList(RequiredLogin, gn.ListView):
    model = Lead
    template_name = "leads/leads-list.html"
    context_object_name = "leads"


class LeadDetail(RequiredLogin, gn.DetailView):
    model = Lead
    template_name = "leads/leads-detail.html"
    pk_url_kwarg = "lead_id"


class LeadDelete(RequiredLogin, gn.DeleteView):
    model = Lead
    pk_url_kwarg = "lead_id"
    template_name = "leads/leads-delete.html"
    success_url = reverse_lazy('leads')


class LeadUpdate(RequiredLogin, gn.UpdateView):
    model = Lead
    form_class = LeadForm
    pk_url_kwarg = "lead_id"
    template_name = "leads/leads-edit.html"
    success_url = reverse_lazy('leads')


class LeadCreate(RequiredLogin, gn.CreateView):
    model = Lead
    form_class = LeadForm
    template_name = "leads/leads-create.html"

    def form_valid(self, form):
        ads = form.cleaned_data['ads']
        object = Advertisement.objects.get(name=ads)
        object.leads_count += 1
        object.save()
        form.save()
        return redirect('leads')
