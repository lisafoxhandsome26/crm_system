from django.shortcuts import render
from ..models import list_customers, list_ads, list_pr, list_contracts, list_leads


def index(request):
    data = {
        "products_count": len(list_pr),
        "advertisements_count": len(list_ads),
        "leads_count": len(list_leads),
        "customers_count": len(list_customers),
        "contracts_count": len(list_contracts)
    }
    return render(request, "users/index.html", context=data)


def login(request):
    return render(request, "registration/login.html")
