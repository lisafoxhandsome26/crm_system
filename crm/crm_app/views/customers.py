from django.shortcuts import render
from django.http import Http404
from ..models import finder, list_customers


def customers_list(request):
    data = {"customers": list_customers}
    return render(request, "customers/customers-list.html", context=data)


def get_customer(request, customer_id: int):
    customer = finder(customer_id, list_customers)
    if customer:
        data = {"object": customer}
        return render(request, "customers/customers-detail.html", context=data)
    else:
        raise Http404()


def delete_customer(request, customer_id: int):
    customer = finder(customer_id, list_customers)
    if customer:
        data = {"object": customer}
        return render(request, "customers/customers-delete.html", context=data)
    else:
        raise Http404()


def edit_customer(request, customer_id: int):
    customer = finder(customer_id, list_customers)
    if customer:
        data = {"object": customer}
        return render(request, "customers/customers-edit.html", context=data)
    else:
        raise Http404()


def create_customer(request):
    return render(request, "customers/customers-create.html")