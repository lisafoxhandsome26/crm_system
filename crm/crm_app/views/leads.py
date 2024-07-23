from django.shortcuts import render
from django.http import Http404
from ..models import finder, list_leads


def leads_list(request):
    data = {"leads": list_leads}
    return render(request, "leads/leads-list.html", context=data)


def get_lead(request, lead_id: int):
    lead = finder(lead_id, list_leads)
    if lead:
        data = {"object": lead}
        return render(request, "leads/leads-detail.html", context=data)
    else:
        raise Http404()


def delete_lead(request, lead_id: int):
    lead = finder(lead_id, list_leads)
    if lead:
        data = {"object": lead}
        return render(request, "leads/leads-delete.html", context=data)
    else:
        raise Http404()


def edit_lead(request, lead_id: int):
    lead = finder(lead_id, list_leads)
    if lead:
        data = {"object": lead}
        return render(request, "leads/leads-edit.html", context=data)
    else:
        raise Http404()


def create_lead(request):
    return render(request, "leads/leads-create.html")