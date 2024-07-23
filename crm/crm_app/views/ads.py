from django.shortcuts import render
from django.http import Http404
from ..models import finder, list_ads


def advertisements_list(request):
    data = {"ads": list_ads}
    return render(request, "ads/ads-list.html", context=data)


def get_ads_statistic(request):
    data = {"ads": list_ads}
    return render(request, "ads/ads-statistic.html", context=data)


def get_advertisements(request, ads_id: int):
    ads = finder(ads_id, list_ads)
    if ads:
        data = {"object": ads}
        return render(request, "ads/ads-detail.html", context=data)
    else:
        raise Http404()


def delete_advertisements(request, ads_id: int):
    ads = finder(ads_id, list_ads)
    if ads:
        data = {"object": ads}
        return render(request, "ads/ads-delete.html", context=data)
    else:
        raise Http404()


def edit_advertisements(request, ads_id: int):
    ads = finder(ads_id, list_ads)
    if ads:
        data = {"object": ads}
        return render(request, "ads/ads-edit.html", context=data)
    else:
        raise Http404()


def create_advertisements(request):
    return render(request, "ads/ads-create.html")