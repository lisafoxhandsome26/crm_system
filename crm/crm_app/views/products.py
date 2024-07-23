from django.shortcuts import render
from django.http import Http404
from ..models import finder, list_pr


def products_list(request):
    data = {"products": list_pr}
    return render(request, "products/products-list.html", context=data)


def create_product(request):
    return render(request, "products/products-create.html")


def delete_product(request, product_id: int):
    product = finder(product_id, list_pr)
    if product:
        data = {"object": product}
        return render(request, "products/products-delete.html", context=data)
    else:
        raise Http404()


def get_product(request, product_id: int):
    product = finder(product_id, list_pr)
    if product:
        data = {"object": product}
        return render(request, "products/products-detail.html", context=data)
    else:
        raise Http404()


def edit_product(request, product_id: int):
    product = finder(product_id, list_pr)
    if product:
        data = {"object": product}
        return render(request, "products/products-edit.html", context=data)
    else:
        raise Http404()
