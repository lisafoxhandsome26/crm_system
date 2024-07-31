from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as gn
from ..models import Advertisement
from ..forms import AdvertisementForm


class RequiredLogin(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = reverse_lazy('login')


class AdvertisementsStatistic(RequiredLogin, gn.ListView):
    model = Advertisement
    permission_required = ["crm_app.view_advertisement"]
    permission_denied_message = "Доступ запрещен"
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"


class AdvertisementsList(RequiredLogin, gn.ListView):
    model = Advertisement
    permission_required = ["crm_app.view_advertisement"]
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdvertisementsDetail(RequiredLogin, gn.DetailView):
    model = Advertisement
    permission_required = ["crm_app.view_advertisement"]
    template_name = "ads/ads-detail.html"
    pk_url_kwarg = "ads_id"


class AdvertisementsDelete(RequiredLogin, gn.DeleteView):
    model = Advertisement
    permission_required = ["crm_app.delete_advertisement"]
    template_name = "ads/ads-delete.html"
    pk_url_kwarg = "ads_id"
    success_url = reverse_lazy('ads')


class AdvertisementsCreate(RequiredLogin, gn.CreateView):
    model = Advertisement
    permission_required = ["crm_app.add_advertisement"]
    template_name = "ads/ads-create.html"
    form_class = AdvertisementForm
    success_url = reverse_lazy('ads')


class AdvertisementsUpdate(RequiredLogin, gn.UpdateView):
    model = Advertisement
    permission_required = ["crm_app.change_advertisement"]
    template_name = "ads/ads-edit.html"
    form_class = AdvertisementForm
    pk_url_kwarg = "ads_id"
    success_url = reverse_lazy('ads')
