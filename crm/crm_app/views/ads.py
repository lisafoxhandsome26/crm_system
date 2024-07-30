from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as gn
from ..models import Advertisement
from ..forms import AdvertisementForm


class RequiredLogin(LoginRequiredMixin):
    login_url = reverse_lazy('login')


class AdvertisementsStatistic(RequiredLogin, gn.ListView):
    model = Advertisement
    template_name = "ads/ads-statistic.html"
    context_object_name = "ads"


class AdvertisementsList(RequiredLogin, gn.ListView):
    model = Advertisement
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdvertisementsDetail(RequiredLogin, gn.DetailView):
    model = Advertisement
    template_name = "ads/ads-detail.html"
    pk_url_kwarg = "ads_id"


class AdvertisementsDelete(RequiredLogin, gn.DeleteView):
    model = Advertisement
    pk_url_kwarg = "ads_id"
    template_name = "ads/ads-delete.html"
    success_url = reverse_lazy('ads')


class AdvertisementsCreate(RequiredLogin, gn.CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy('ads')


class AdvertisementsUpdate( gn.UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    pk_url_kwarg = "ads_id"
    template_name = "ads/ads-edit.html"
    success_url = reverse_lazy('ads')
